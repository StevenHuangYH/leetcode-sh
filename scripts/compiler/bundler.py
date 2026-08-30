import re
from pathlib import Path
from typing import Optional
from .entities import read_file

class TemplateBundler:
    """In-memory template bundler that inlines modular CSS/JS assets into a self-contained SPA template."""

    def __init__(self, templates_dir: Optional[Path] = None):
        if templates_dir is None:
            self.templates_dir = Path(__file__).parent.parent.parent / "templates"
        else:
            self.templates_dir = Path(templates_dir)

    def bundle(self) -> str:
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
                return read_file(asset_path)
            return f"/* Missing asset: {asset_rel} */"

        bundled = re.sub(r'<!--\s*@inject:\s*([^>\s]+)\s*-->', inject_handler, layout_content)
        return bundled
