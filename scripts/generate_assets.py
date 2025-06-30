#!/usr/bin/env python3
"""
Generate various asset formats from SVG icons.

This script converts SVG icons to PNG, ICO, and other formats for different use cases:
- PNG files in various sizes for web usage
- Favicon files (ICO format with multiple sizes)
- OpenGraph images for social media
"""

import os
import sys
from pathlib import Path
from PIL import Image, ImageDraw
import cairosvg
import io


class AssetGenerator:
    def __init__(self, input_dir="v2", output_dir="assets"):
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.png_dir = self.output_dir / "png"
        self.favicon_dir = self.output_dir / "favicon"
        self.opengraph_dir = self.output_dir / "opengraph"
        
        # Create output directories
        self.png_dir.mkdir(parents=True, exist_ok=True)
        self.favicon_dir.mkdir(parents=True, exist_ok=True)
        self.opengraph_dir.mkdir(parents=True, exist_ok=True)
        
        # Define size configurations
        self.png_sizes = [16, 24, 32, 48, 64, 96, 128, 192, 256, 512, 1024]
        self.favicon_sizes = [16, 24, 32, 48, 64]
        self.opengraph_sizes = [
            (1200, 630),  # OpenGraph standard
            (1200, 1200), # Square for social media
            (800, 800),   # Instagram square
            (1080, 1080), # Instagram post
            (1200, 675),  # Twitter card
        ]

    def svg_to_png(self, svg_path, output_path, width, height=None):
        """Convert SVG to PNG with specified dimensions."""
        if height is None:
            height = width
            
        try:
            # Convert SVG to PNG using cairosvg
            png_data = cairosvg.svg2png(
                url=str(svg_path),
                output_width=width,
                output_height=height
            )
            
            # Save PNG
            with open(output_path, 'wb') as f:
                f.write(png_data)
            
            print(f"✓ Generated {output_path} ({width}x{height})")
            return True
            
        except Exception as e:
            print(f"✗ Error generating {output_path}: {e}")
            return False

    def create_favicon(self, png_files, output_path):
        """Create a multi-size ICO file from PNG files."""
        try:
            images = []
            for png_path in png_files:
                if png_path.exists():
                    img = Image.open(png_path)
                    # Ensure RGBA mode for ICO
                    if img.mode != 'RGBA':
                        img = img.convert('RGBA')
                    images.append(img)
            
            if images:
                # Save as ICO with multiple sizes
                images[0].save(
                    output_path,
                    format='ICO',
                    sizes=[(img.width, img.height) for img in images]
                )
                print(f"✓ Generated {output_path} with {len(images)} sizes")
                return True
            else:
                print(f"✗ No valid PNG files found for {output_path}")
                return False
                
        except Exception as e:
            print(f"✗ Error creating favicon {output_path}: {e}")
            return False

    def generate_png_assets(self, svg_file):
        """Generate PNG files in various sizes."""
        print(f"\n📱 Generating PNG assets from {svg_file.name}...")
        
        base_name = svg_file.stem
        success_count = 0
        
        for size in self.png_sizes:
            output_file = self.png_dir / f"{base_name}-{size}x{size}.png"
            if self.svg_to_png(svg_file, output_file, size):
                success_count += 1
        
        print(f"📱 PNG Generation: {success_count}/{len(self.png_sizes)} successful")
        return success_count

    def generate_favicon_assets(self, svg_file):
        """Generate favicon files."""
        print(f"\n🔖 Generating favicon assets from {svg_file.name}...")
        
        base_name = svg_file.stem
        
        # Generate PNG files for favicon sizes
        png_files = []
        for size in self.favicon_sizes:
            output_file = self.favicon_dir / f"{base_name}-{size}x{size}.png"
            if self.svg_to_png(svg_file, output_file, size):
                png_files.append(output_file)
        
        # Create ICO file
        ico_file = self.favicon_dir / f"{base_name}.ico"
        self.create_favicon(png_files, ico_file)
        
        # Also create a standard favicon.ico
        if base_name == "icon":
            standard_favicon = self.favicon_dir / "favicon.ico"
            self.create_favicon(png_files, standard_favicon)
        
        print(f"🔖 Favicon Generation: Complete")

    def generate_opengraph_assets(self, svg_file):
        """Generate OpenGraph images for social media."""
        print(f"\n🌐 Generating OpenGraph assets from {svg_file.name}...")
        
        base_name = svg_file.stem
        success_count = 0
        
        for width, height in self.opengraph_sizes:
            output_file = self.opengraph_dir / f"{base_name}-{width}x{height}.png"
            if self.svg_to_png(svg_file, output_file, width, height):
                success_count += 1
        
        print(f"🌐 OpenGraph Generation: {success_count}/{len(self.opengraph_sizes)} successful")
        return success_count

    def generate_assets_from_svg(self, svg_file):
        """Generate all asset types from a single SVG file."""
        print(f"\n{'='*60}")
        print(f"🎨 Processing: {svg_file}")
        print(f"{'='*60}")
        
        if not svg_file.exists():
            print(f"✗ SVG file not found: {svg_file}")
            return False
        
        # Skip animated SVG for static assets
        if "animate" in svg_file.stem:
            print(f"⏭️  Skipping animated SVG: {svg_file.name}")
            return True
        
        # Generate different asset types
        png_count = self.generate_png_assets(svg_file)
        self.generate_favicon_assets(svg_file)
        og_count = self.generate_opengraph_assets(svg_file)
        
        total_generated = png_count + og_count
        print(f"\n✅ Total assets generated: {total_generated}")
        return True

    def generate_all(self):
        """Generate assets from all SVG files in the input directory."""
        print("🚀 Starting asset generation...")
        print(f"📁 Input directory: {self.input_dir}")
        print(f"📁 Output directory: {self.output_dir}")
        
        svg_files = list(self.input_dir.glob("*.svg"))
        
        if not svg_files:
            print(f"❌ No SVG files found in {self.input_dir}")
            return False
        
        print(f"📋 Found {len(svg_files)} SVG files:")
        for svg_file in svg_files:
            print(f"   - {svg_file.name}")
        
        success_count = 0
        for svg_file in svg_files:
            if self.generate_assets_from_svg(svg_file):
                success_count += 1
        
        print(f"\n{'='*60}")
        print(f"🎉 Asset generation complete!")
        print(f"📊 Successfully processed: {success_count}/{len(svg_files)} files")
        print(f"{'='*60}")
        
        return success_count == len(svg_files)

    def create_readme(self):
        """Create README for the assets directory."""
        readme_content = """# Generated Assets

This directory contains automatically generated assets from the SVG icons in the `v2/` directory.

## Directory Structure

```
assets/
├── png/          # PNG files in various sizes
├── favicon/      # Favicon files (ICO format)
├── opengraph/    # OpenGraph images for social media
└── README.md     # This file
```

## PNG Assets

PNG files are generated in the following sizes:
- **16x16** - Small icon
- **24x24** - Small icon
- **32x32** - Standard icon
- **48x48** - Standard icon
- **64x64** - Standard icon
- **96x96** - Medium icon
- **128x128** - Medium icon
- **192x192** - Large icon (Android)
- **256x256** - Large icon
- **512x512** - Extra large icon
- **1024x1024** - Maximum size

## Favicon Assets

Favicon files include:
- **favicon.ico** - Multi-size ICO file (16, 24, 32, 48, 64px)
- **icon.ico** - Same as favicon.ico
- Individual PNG files for each size

## OpenGraph Assets

OpenGraph images for social media:
- **1200x630** - Standard OpenGraph
- **1200x1200** - Square social media
- **800x800** - Instagram square
- **1080x1080** - Instagram post
- **1200x675** - Twitter card

## Usage

### HTML Favicon
```html
<link rel="icon" type="image/x-icon" href="/assets/favicon/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/favicon/icon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/assets/favicon/icon-16x16.png">
```

### OpenGraph Meta Tags
```html
<meta property="og:image" content="/assets/opengraph/icon-1200x630.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
```

### PNG Icons
```html
<img src="/assets/png/icon-64x64.png" alt="Die Coding Technology Logo" width="64" height="64">
```

---

*This file is automatically generated. Do not edit manually.*
"""
        
        readme_path = self.output_dir / "README.md"
        with open(readme_path, 'w') as f:
            f.write(readme_content)
        
        print(f"📝 Generated {readme_path}")


def main():
    """Main function."""
    generator = AssetGenerator()
    
    # Generate all assets
    success = generator.generate_all()
    
    # Create documentation
    generator.create_readme()
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
