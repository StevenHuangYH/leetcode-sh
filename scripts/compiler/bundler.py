import re
from pathlib import Path
from typing import Optional
from .entities import read_file

def minify_css(css: str) -> str:
    """Strips comments and unnecessary whitespace from CSS."""
    css = re.sub(r'/\*.*?\*/', '', css, flags=re.DOTALL)
    css = re.sub(r'\s+', ' ', css)
    css = re.sub(r'\s*([\{\};:,>])\s*', r'\1', css)
    return css.strip()

def minify_js(js: str) -> str:
    """Strips comments and blank lines from JavaScript."""
    js = re.sub(r'/\*.*?\*/', '', js, flags=re.DOTALL)
    lines = []
    for line in js.splitlines():
        stripped = line.strip()
        if stripped.startswith("//"):
            continue
        if stripped:
            lines.append(line)
    return "\n".join(lines)

class TemplateBundler:
    """In-memory template bundler that inlines modular CSS/JS assets into a self-contained SPA template."""

    def __init__(self, templates_dir: Optional[Path] = None):
        if templates_dir is None:
            self.templates_dir = Path(__file__).parent.parent.parent / "templates"
        else:
            self.templates_dir = Path(templates_dir)

    def bundle(self, minify: bool = True) -> str:
        """Bundles modular layout and asset sources into a single template string."""
        layout_path = self.templates_dir / "src" / "layout.html"
        if not layout_path.exists():
            # Fallback to monolithic station_template.html
            fallback_path = self.templates_dir / "station_template.html"
            return read_file(fallback_path)

        layout_content = read_file(layout_path)
        src_dir = self.templates_dir / "src"

        def inject_handler(match: re.Match) -> str:
            asset_rel = match.group(1).strip()
            asset_path = src_dir / asset_rel
            if asset_path.exists():
                content = read_file(asset_path)
                if minify:
                    if asset_rel.endswith(".css"):
                        return minify_css(content)
                    elif asset_rel.endswith(".js"):
                        return minify_js(content)
                return content
            return f"/* Missing asset: {asset_rel} */"

        bundled = re.sub(r'<!--\s*@inject:\s*([^>\s]+)\s*-->', inject_handler, layout_content)
        return bundled
