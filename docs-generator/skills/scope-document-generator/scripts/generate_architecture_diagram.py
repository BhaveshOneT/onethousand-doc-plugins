#!/usr/bin/env python3
"""
Generate professional architecture diagrams using Graphviz.

Produces diagrams with grouped zones, typed component shapes,
colour-coded nodes, and labelled data-flow arrows — matching the
quality of hand-crafted architecture diagrams.

Rendering pipeline (automatic fallback):
  1. Graphviz ``dot``  (best quality — zones, shapes, arrow routing)
  2. Pillow PNG         (basic grid if Graphviz is missing)

Usage:
    python generate_architecture_diagram.py \\
        --description <desc.json> --output <diagram.png> [--style detailed]

Example description.json:
{
  "title": "System Architecture",
  "zones": [
    {
      "name": "On Premise Architecture",
      "components": ["SQL Database", "Email Inboxes", "SAP Endpoint"]
    },
    {
      "name": "Azure Virtual Network",
      "color": "#0078D4",
      "components": ["VPN Gateway", "Quotation Pipeline", "LLM Endpoint",
                      "Webapp", "Draft DB"]
    }
  ],
  "components": [
    {"name": "SQL Database",        "type": "database"},
    {"name": "Email Inboxes",       "type": "client"},
    {"name": "SAP Endpoint",        "type": "external"},
    {"name": "VPN Gateway",         "type": "gateway"},
    {"name": "Quotation Pipeline",  "type": "service"},
    {"name": "LLM Endpoint",        "type": "ai"},
    {"name": "Webapp",              "type": "client"},
    {"name": "Draft DB",            "type": "database"}
  ],
  "flows": [
    {"from": "Email Inboxes",       "to": "VPN Gateway",         "label": "Read emails"},
    {"from": "SQL Database",        "to": "VPN Gateway",         "label": "Load relevant data"},
    {"from": "VPN Gateway",         "to": "Quotation Pipeline",  "label": ""},
    {"from": "Quotation Pipeline",  "to": "LLM Endpoint",        "label": "LLM information extraction"},
    {"from": "Quotation Pipeline",  "to": "Draft DB",            "label": "Store quotations"},
    {"from": "Webapp",              "to": "Draft DB",            "label": "Fetch quotations"},
    {"from": "Webapp",              "to": "SAP Endpoint",        "label": "Save confirmed quotations"}
  ]
}

Component types → Graphviz shapes:
  client    → box (rounded)        light blue
  service   → box (rounded)        light purple
  database  → cylinder             light green
  external  → component            light orange
  gateway   → box3d                light purple
  ai        → doubleoctagon        light blue
  queue     → parallelogram        light lime
  cache     → octagon              light pink
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# ---------------------------------------------------------------------------
# Graphviz shape / colour mappings
# ---------------------------------------------------------------------------

SHAPE_MAP = {
    "client":   "box",
    "service":  "box",
    "database": "cylinder",
    "external": "component",
    "gateway":  "box3d",
    "ai":       "doubleoctagon",
    "queue":    "parallelogram",
    "cache":    "octagon",
    "message":  "cds",
}

FILL_MAP = {
    "client":   "#E1F5FF",
    "service":  "#F3E5F5",
    "database": "#E8F5E9",
    "external": "#FFF3E0",
    "gateway":  "#F3E5F5",
    "ai":       "#E3F2FD",
    "queue":    "#F1F8E9",
    "cache":    "#FCE4EC",
    "message":  "#FCE4EC",
}

BORDER_MAP = {
    "client":   "#01579B",
    "service":  "#4A148C",
    "database": "#1B5E20",
    "external": "#E65100",
    "gateway":  "#4A148C",
    "ai":       "#0D47A1",
    "queue":    "#33691E",
    "cache":    "#880E4F",
    "message":  "#880E4F",
}

DEFAULT_ZONE_COLOR = "#999999"
DEFAULT_ZONE_BG    = "#FAFAFA"


def _safe_id(name: str) -> str:
    """Convert a display name into a valid Graphviz identifier."""
    return re.sub(r"[^a-zA-Z0-9]", "_", name)


def _escape_label(text: str) -> str:
    """Escape a label for Graphviz DOT (replace newlines with \\n)."""
    return text.replace("\n", "\\n").replace('"', '\\"')


# ---------------------------------------------------------------------------
# Graphviz DOT generation
# ---------------------------------------------------------------------------

def generate_dot(description: Dict[str, Any], style: str = "detailed") -> str:
    """Build a Graphviz DOT string from an architecture description dict."""

    title = description.get("title", "System Architecture")
    components = {c["name"]: c for c in description.get("components", [])}
    zones = description.get("zones", [])
    flows = description.get("flows", [])

    lines: List[str] = []
    lines.append("digraph architecture {")

    # --- Graph-level attributes ---
    lines.append('    graph [')
    lines.append('        rankdir=LR')
    lines.append('        fontname="DejaVu Sans"')
    lines.append('        fontsize=11')
    lines.append('        bgcolor=white')
    lines.append('        pad=0.5')
    lines.append('        nodesep=0.6')
    lines.append('        ranksep=1.2')
    lines.append('        label=""')
    lines.append('        dpi=150')
    lines.append('    ]')

    lines.append('    node [')
    lines.append('        fontname="DejaVu Sans"')
    lines.append('        fontsize=10')
    lines.append('        style="filled,rounded"')
    lines.append('        shape=box')
    lines.append('        penwidth=1.5')
    lines.append('    ]')

    lines.append('    edge [')
    lines.append('        fontname="DejaVu Sans"')
    lines.append('        fontsize=8')
    lines.append('        color="#666666"')
    lines.append('        penwidth=1.2')
    lines.append('    ]')
    lines.append("")

    # Track which components have been placed in zones
    placed = set()

    # --- Zones (subgraph clusters) ---
    for zi, zone in enumerate(zones):
        zone_name = zone.get("name", f"Zone {zi}")
        zone_color = zone.get("color", DEFAULT_ZONE_COLOR)
        zone_bg = zone.get("bgcolor", DEFAULT_ZONE_BG if zone_color == DEFAULT_ZONE_COLOR else _lighten(zone_color))
        zone_comps = zone.get("components", [])

        lines.append(f'    subgraph cluster_{zi} {{')
        lines.append(f'        label="{_escape_label(zone_name)}"')
        lines.append(f'        labeljust=l')
        lines.append(f'        fontsize=11')
        lines.append(f'        fontname="DejaVu Sans Bold"')
        lines.append(f'        style="rounded,dashed"')
        lines.append(f'        color="{zone_color}"')
        lines.append(f'        bgcolor="{zone_bg}"')
        lines.append(f'        penwidth=1.5')
        lines.append("")

        for comp_name in zone_comps:
            comp = components.get(comp_name)
            if comp:
                lines.append(f"        {_node_def(comp, style)}")
                placed.add(comp_name)

        lines.append("    }")
        lines.append("")

    # --- Ungrouped components ---
    for name, comp in components.items():
        if name not in placed:
            lines.append(f"    {_node_def(comp, style)}")

    lines.append("")

    # --- Flows (edges) ---
    for flow in flows:
        from_id = _safe_id(flow["from"])
        to_id = _safe_id(flow["to"])
        label = flow.get("label", "")
        direction = flow.get("dir", "")  # e.g. "both"

        attrs: List[str] = []
        if label:
            attrs.append(f'label="{_escape_label(label)}"')
        if direction:
            attrs.append(f'dir={direction}')

        attr_str = f" [{', '.join(attrs)}]" if attrs else ""
        lines.append(f"    {from_id} -> {to_id}{attr_str}")

    lines.append("}")
    return "\n".join(lines)


def _node_def(comp: Dict[str, Any], style: str) -> str:
    """Return a single Graphviz node definition line."""
    name = comp["name"]
    ctype = comp.get("type", "service")
    node_id = _safe_id(name)

    shape = SHAPE_MAP.get(ctype, "box")
    fill = FILL_MAP.get(ctype, "#F5F5F5")
    border = BORDER_MAP.get(ctype, "#333333")

    # Build label: use explicit label or name with \n for line breaks
    label = comp.get("label", name.replace(" ", "\\n"))

    parts = [
        f'{node_id} [',
        f'label="{label}"',
        f'shape={shape}',
        f'fillcolor="{fill}"',
        f'color="{border}"',
    ]

    if style == "detailed" and comp.get("description"):
        # Could add tooltip or subtitle later
        pass

    return " ".join(parts) + "]"


def _lighten(hex_color: str) -> str:
    """Return a very light tint of the given hex colour for zone background."""
    hex_color = hex_color.lstrip("#")
    try:
        r, g, b = int(hex_color[:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        # Blend 85% white
        r = int(r * 0.15 + 255 * 0.85)
        g = int(g * 0.15 + 255 * 0.85)
        b = int(b * 0.15 + 255 * 0.85)
        return f"#{r:02X}{g:02X}{b:02X}"
    except (ValueError, IndexError):
        return DEFAULT_ZONE_BG


# ---------------------------------------------------------------------------
# Rendering
# ---------------------------------------------------------------------------

def render_with_graphviz(dot_source: str, output_path: str, dpi: int = 150) -> bool:
    """Render a DOT string to PNG using the ``dot`` command."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".dot", delete=False) as f:
        f.write(dot_source)
        dot_file = f.name

    try:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        cmd = ["dot", f"-Gdpi={dpi}", "-Tpng", dot_file, "-o", output_path]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)

        if result.returncode != 0:
            print(f"Graphviz error: {result.stderr}")
            return False

        print(f"Generated diagram with Graphviz: {output_path}")
        return True

    except FileNotFoundError:
        print("Graphviz 'dot' command not found")
        return False
    except subprocess.TimeoutExpired:
        print("Graphviz rendering timed out")
        return False
    except Exception as e:
        print(f"Graphviz error: {e}")
        return False
    finally:
        try:
            os.unlink(dot_file)
        except OSError:
            pass


def render_with_pillow(description: Dict[str, Any], output_path: str) -> bool:
    """Basic Pillow PNG fallback (grid layout, no zones)."""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("Pillow not available for fallback rendering")
        return False

    try:
        components = description.get("components", [])
        flows = description.get("flows", [])
        title = description.get("title", "System Architecture")

        W, H = 1200, 800
        comp_w, comp_h = 180, 70
        img = Image.new("RGB", (W, H), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)

        try:
            font_title = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 22)
            font_name = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 12)
            font_small = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 10)
        except (IOError, OSError):
            font_title = font_name = font_small = ImageFont.load_default()

        draw.text((24, 16), title, fill=(50, 50, 50), font=font_title)

        # Simple grid layout
        n = len(components)
        cols = max(2, int(n ** 0.5) + 1)
        for i, comp in enumerate(components):
            row, col = divmod(i, cols)
            x = 60 + col * (comp_w + 40)
            y = 70 + row * (comp_h + 50)
            fill_rgb = _hex_to_rgb(FILL_MAP.get(comp.get("type", "service"), "#F5F5F5"))
            border_rgb = _hex_to_rgb(BORDER_MAP.get(comp.get("type", "service"), "#333333"))
            draw.rounded_rectangle((x, y, x + comp_w, y + comp_h), radius=8,
                                   fill=fill_rgb, outline=border_rgb, width=2)
            name = comp["name"]
            bb = draw.textbbox((0, 0), name, font=font_name)
            tw = bb[2] - bb[0]
            draw.text((x + comp_w // 2 - tw // 2, y + comp_h // 2 - 8), name,
                      fill=(0, 0, 0), font=font_name)

        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        img.save(output_path, "PNG", dpi=(150, 150))
        print(f"Generated Pillow fallback diagram: {output_path}")
        return True

    except Exception as e:
        print(f"Pillow fallback error: {e}")
        return False


def _hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
    h = hex_color.lstrip("#")
    return (int(h[:2], 16), int(h[2:4], 16), int(h[4:6], 16))


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def load_description(json_path: str) -> Optional[Dict[str, Any]]:
    """Load architecture description from a JSON file."""
    try:
        with open(json_path) as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: file not found: {json_path}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: invalid JSON: {e}")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Generate architecture diagrams from JSON descriptions",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Component types: client, service, database, external, gateway, ai, queue, cache, message

Usage examples:
  %(prog)s -d arch.json -o diagram.png
  %(prog)s -d arch.json -o diagram.png --style detailed --dpi 200
        """,
    )
    parser.add_argument("-d", "--description", required=True, help="JSON description file")
    parser.add_argument("-o", "--output", required=True, help="Output PNG path")
    parser.add_argument("-s", "--style", choices=["default", "detailed"], default="detailed")
    parser.add_argument("--dpi", type=int, default=150, help="Output DPI (default 150)")

    args = parser.parse_args()

    description = load_description(args.description)
    if not description:
        sys.exit(1)

    comps = description.get("components", [])
    flows = description.get("flows", [])
    print(f"Loaded {len(comps)} components and {len(flows)} flows")

    # Ensure output ends in .png
    output = args.output
    if not output.lower().endswith(".png"):
        output = output.rsplit(".", 1)[0] + ".png"

    # 1. Try Graphviz
    dot_source = generate_dot(description, style=args.style)
    print("\nGenerated DOT source:")
    print(dot_source)
    print()

    if render_with_graphviz(dot_source, output, dpi=args.dpi):
        print("Success!")
        sys.exit(0)

    # 2. Pillow fallback
    print("Falling back to Pillow renderer...")
    if render_with_pillow(description, output):
        print("Success (Pillow fallback)!")
        sys.exit(0)

    print("Error: all renderers failed")
    sys.exit(1)


if __name__ == "__main__":
    main()
