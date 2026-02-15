#!/usr/bin/env python3
"""
Extract architecture diagram images from hackathon documents (PDF or DOCX).

Usage:
    python extract_architecture_diagram.py --input <file.pdf|file.docx> --output <image.png> [--page <page_num>]

Examples:
    # Extract from PDF (auto-detect best image)
    python extract_architecture_diagram.py --input hackathon.pdf --output diagram.png

    # Extract from specific PDF page
    python extract_architecture_diagram.py --input hackathon.pdf --output diagram.png --page 5

    # Extract from DOCX
    python extract_architecture_diagram.py --input proposal.docx --output diagram.png
"""

import argparse
import io
import os
import sys
import tempfile
import zipfile
from pathlib import Path


def extract_from_pdf_pdfplumber(pdf_path: str, page_num: int = None) -> bytes:
    """Extract images from PDF using pdfplumber."""
    try:
        import pdfplumber
    except ImportError:
        return None

    try:
        with pdfplumber.open(pdf_path) as pdf:
            total_pages = len(pdf.pages)

            # Determine which pages to search
            if page_num is not None:
                if page_num < 1 or page_num > total_pages:
                    print(f"Error: Page {page_num} out of range (1-{total_pages})")
                    return None
                pages_to_search = [pdf.pages[page_num - 1]]
            else:
                # Skip first 2 pages, search from page 3 onwards
                pages_to_search = pdf.pages[2:] if len(pdf.pages) > 2 else pdf.pages

            largest_image = None
            largest_size = 0

            for page_idx, page in enumerate(pages_to_search):
                for image in page.images:
                    if image:
                        # Get image size
                        img_bytes = image['stream'].get_data()
                        img_size = len(img_bytes)

                        if img_size > largest_size:
                            largest_size = img_size
                            largest_image = img_bytes
                            page_found = (page_idx + (3 if page_num is None else page_num))

            if largest_image:
                print(f"Found architecture diagram ({largest_size} bytes)")
                return largest_image
            else:
                print("No images found in PDF")
                return None

    except Exception as e:
        print(f"Error reading PDF with pdfplumber: {e}")
        return None


def extract_from_pdf_fitz(pdf_path: str, page_num: int = None) -> bytes:
    """Extract images from PDF using PyMuPDF (fitz)."""
    try:
        import fitz
    except ImportError:
        return None

    try:
        doc = fitz.open(pdf_path)
        total_pages = len(doc)

        # Determine which pages to search
        if page_num is not None:
            if page_num < 1 or page_num > total_pages:
                print(f"Error: Page {page_num} out of range (1-{total_pages})")
                return None
            pages_to_search = [page_num - 1]
        else:
            # Skip first 2 pages, search from page 3 onwards
            pages_to_search = list(range(2, total_pages)) if total_pages > 2 else list(range(total_pages))

        largest_image = None
        largest_size = 0

        for page_idx in pages_to_search:
            page = doc[page_idx]
            image_list = page.get_images()

            for img_index in image_list:
                xref = img_index[0]
                pix = fitz.Pixmap(doc, xref)

                if pix.n - pix.alpha < 4:  # GRAY or RGB
                    img_data = pix.tobytes("png")
                else:  # CMYK
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                    img_data = pix.tobytes("png")

                img_size = len(img_data)
                if img_size > largest_size:
                    largest_size = img_size
                    largest_image = img_data

        if largest_image:
            print(f"Found architecture diagram ({largest_size} bytes)")
            return largest_image
        else:
            print("No images found in PDF")
            return None

    except Exception as e:
        print(f"Error reading PDF with PyMuPDF: {e}")
        return None


def extract_from_pdf_zipmethod(pdf_path: str, page_num: int = None) -> bytes:
    """Fallback: Extract images from PDF by treating it as a ZIP archive."""
    try:
        with zipfile.ZipFile(pdf_path, 'r') as pdf_zip:
            # PDFs have embedded images/media
            image_files = [f for f in pdf_zip.namelist()
                          if f.startswith(('PDF/')) or 'Image' in f or 'image' in f]

            if image_files:
                # Try to get the largest image
                largest = max(image_files, key=lambda f: len(pdf_zip.read(f)))
                img_data = pdf_zip.read(largest)
                print(f"Found architecture diagram via ZIP extraction ({len(img_data)} bytes)")
                return img_data
    except (zipfile.BadZipFile, Exception):
        pass

    return None


def extract_from_pdf(pdf_path: str, page_num: int = None) -> bytes:
    """Extract images from PDF with fallback mechanisms."""
    print(f"Extracting from PDF: {pdf_path}")

    # Try pdfplumber first
    result = extract_from_pdf_pdfplumber(pdf_path, page_num)
    if result:
        return result

    print("pdfplumber not available, trying PyMuPDF...")

    # Try PyMuPDF
    result = extract_from_pdf_fitz(pdf_path, page_num)
    if result:
        return result

    print("PyMuPDF not available, trying ZIP-based extraction...")

    # Try ZIP method
    result = extract_from_pdf_zipmethod(pdf_path, page_num)
    if result:
        return result

    return None


def extract_from_docx(docx_path: str) -> bytes:
    """Extract images from DOCX file."""
    print(f"Extracting from DOCX: {docx_path}")

    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            # DOCX is a ZIP archive
            with zipfile.ZipFile(docx_path, 'r') as docx_zip:
                # Extract all files
                docx_zip.extractall(tmpdir)

                # Look for images in word/media/
                media_dir = Path(tmpdir) / "word" / "media"

                if not media_dir.exists():
                    print("No word/media directory found in DOCX")
                    return None

                # Get all images, sorted by name (natural order)
                image_files = sorted([f for f in media_dir.iterdir() if f.is_file()])

                if not image_files:
                    print("No images found in word/media/")
                    return None

                # Skip first image (usually logo), take largest remaining
                if len(image_files) > 1:
                    candidates = image_files[1:]
                else:
                    candidates = image_files

                # Find largest image
                largest_file = max(candidates, key=lambda f: f.stat().st_size)

                with open(largest_file, 'rb') as f:
                    img_data = f.read()

                print(f"Found architecture diagram: {largest_file.name} ({len(img_data)} bytes)")
                return img_data

    except zipfile.BadZipFile:
        print("Error: Invalid DOCX file (not a valid ZIP archive)")
        return None
    except Exception as e:
        print(f"Error extracting from DOCX: {e}")
        return None


def save_image(image_data: bytes, output_path: str) -> bool:
    """Save image data to file."""
    try:
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file, 'wb') as f:
            f.write(image_data)

        print(f"Saved architecture diagram to: {output_path}")
        return True
    except Exception as e:
        print(f"Error saving image: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Extract architecture diagram images from hackathon documents",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Extract from PDF (auto-detect best image)
  %(prog)s --input hackathon.pdf --output diagram.png

  # Extract from specific PDF page
  %(prog)s --input hackathon.pdf --output diagram.png --page 5

  # Extract from DOCX
  %(prog)s --input proposal.docx --output diagram.png
        """
    )

    parser.add_argument(
        '--input', '-i',
        required=True,
        help='Input file (PDF or DOCX)'
    )
    parser.add_argument(
        '--output', '-o',
        required=True,
        help='Output image file (PNG)'
    )
    parser.add_argument(
        '--page', '-p',
        type=int,
        default=None,
        help='Specific page number to extract from (PDF only)'
    )

    args = parser.parse_args()

    # Validate input file
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file not found: {args.input}")
        sys.exit(1)

    file_ext = input_path.suffix.lower()

    # Extract based on file type
    if file_ext == '.pdf':
        image_data = extract_from_pdf(str(input_path), args.page)
    elif file_ext == '.docx':
        if args.page is not None:
            print("Warning: --page argument ignored for DOCX files")
        image_data = extract_from_docx(str(input_path))
    else:
        print(f"Error: Unsupported file type: {file_ext}")
        print("Supported types: .pdf, .docx")
        sys.exit(1)

    # Check if extraction was successful
    if not image_data:
        print("Error: Could not extract architecture diagram from document")
        sys.exit(1)

    # Save the image
    if not save_image(image_data, args.output):
        sys.exit(1)

    print("Success!")
    sys.exit(0)


if __name__ == '__main__':
    main()
