# Asset Generation Guide

## Overview

This project automatically generates multiple asset formats from SVG icons for use across different platforms and contexts.

## What Gets Generated

### 📱 PNG Assets (11 sizes)

- 16x16, 24x24, 32x32, 48x48, 64x64
- 96x96, 128x128, 192x192, 256x256
- 512x512, 1024x1024

### 🔖 Favicon Assets

- **favicon.ico** - Multi-size ICO file
- Individual PNG files for modern browsers
- Perfect cross-browser compatibility

### 🌐 OpenGraph Assets

- **1200x630** - Standard OpenGraph
- **1200x1200** - Square social media
- **800x800** - Instagram square
- **1080x1080** - Instagram post
- **1200x675** - Twitter card

## How to Use

### 🚀 Automatic (GitHub Action)

- Push changes to `main` branch
- Assets are automatically generated
- No manual intervention required

### 🛠️ Manual Generation

```bash
# Method 1: Shell script (recommended)
./generate_assets.sh

# Method 2: Direct Python
python scripts/generate_assets.py

# Method 3: With virtual environment
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/generate_assets.py
```

## HTML Implementation

### Favicon

```html
<link rel="icon" type="image/x-icon" href="assets/favicon/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="assets/favicon/icon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="assets/favicon/icon-16x16.png">
```

### OpenGraph

```html
<meta property="og:image" content="assets/opengraph/icon-1200x630.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:type" content="image/png">
```

### Standard Images

```html
<img src="assets/png/icon-64x64.png" alt="Die Coding Technology" width="64">
```

### CSS Background

```css
.logo {
    background-image: url('assets/png/icon-128x128.png');
    background-size: contain;
    background-repeat: no-repeat;
}
```

## Technical Details

### Dependencies

- **Python 3.8+**
- **cairosvg** - SVG to PNG conversion
- **Pillow** - Image processing and ICO creation
- **librsvg2-bin** (system) - SVG rendering
- **imagemagick** (system) - Image manipulation

### Input Filtering

- Only processes `icon.svg` (static version)
- Skips `icon-animate.svg` to avoid issues with animations
- Maintains clean, consistent output

### Output Structure

```
assets/
├── png/
│   ├── icon-16x16.png
│   ├── icon-24x24.png
│   └── ... (all sizes)
├── favicon/
│   ├── favicon.ico
│   ├── icon.ico
│   └── individual PNGs
├── opengraph/
│   ├── icon-1200x630.png
│   └── ... (all social formats)
└── README.md
```

## Customization

To modify generated sizes, edit `scripts/generate_assets.py`:

```python
# PNG sizes
self.png_sizes = [16, 24, 32, 48, 64, 96, 128, 192, 256, 512, 1024]

# Favicon sizes  
self.favicon_sizes = [16, 24, 32, 48, 64]

# OpenGraph sizes
self.opengraph_sizes = [
    (1200, 630),  # OpenGraph standard
    (1200, 1200), # Square
    # Add more as needed...
]
```

## Troubleshooting

### Common Issues

1. **Permission denied on shell script**

   ```bash
   chmod +x generate_assets.sh
   ```

2. **Missing system dependencies**

   ```bash
   # Ubuntu/Debian
   sudo apt-get install librsvg2-bin imagemagick
   
   # macOS
   brew install librsvg imagemagick
   ```

3. **Python module not found**

   ```bash
   pip install cairosvg pillow
   ```

### Verification

Check if assets were generated correctly:

```bash
ls -la assets/
ls assets/png/ | wc -l    # Should show 11 files
ls assets/favicon/        # Should show ICO and PNG files  
ls assets/opengraph/      # Should show 5 social media formats
```

---

*This documentation is automatically maintained. For issues or suggestions, please open a GitHub issue.*
