#!/usr/bin/env bash
# Check all required Python packages; install only if any are missing
python3 -c "import pdfplumber, docx, PIL, graphviz, pptx, lxml" 2>/dev/null && exit 0
SCRIPT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
pip install -r "$SCRIPT_DIR/requirements.txt" --break-system-packages --quiet 2>/dev/null
