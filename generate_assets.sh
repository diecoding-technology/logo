#!/bin/bash

# Generate Assets Script
# Converts SVG icons to various formats (PNG, ICO, OpenGraph images)

set -e  # Exit on any error

echo "🚀 Die Coding Technology - Asset Generator"
echo "==========================================="

# Check if Python is available
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required but not installed."
    exit 1
fi

# Check if pip is available
if ! python3 -m pip --version &> /dev/null; then
    echo "❌ pip is required but not available."
    exit 1
fi

# Install system dependencies (Linux)
if command -v apt-get &> /dev/null; then
    echo "📦 Installing system dependencies..."
    sudo apt-get update -qq
    sudo apt-get install -y librsvg2-bin imagemagick
elif command -v yum &> /dev/null; then
    echo "📦 Installing system dependencies..."
    sudo yum install -y librsvg2-tools ImageMagick
elif command -v brew &> /dev/null; then
    echo "📦 Installing system dependencies (macOS)..."
    brew install librsvg imagemagick
else
    echo "⚠️  Could not detect package manager. Please install librsvg and imagemagick manually."
fi

# Create virtual environment if it doesn't exist
if [ ! -d ".venv" ]; then
    echo "🐍 Creating Python virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
echo "🔌 Activating virtual environment..."
source .venv/bin/activate

# Install Python dependencies
echo "📥 Installing Python dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Create output directories
echo "📁 Creating output directories..."
mkdir -p assets/{png,favicon,opengraph}

# Run the generator
echo "⚙️  Running asset generator..."
python scripts/generate_assets.py

echo ""
echo "✅ Asset generation complete!"
echo "📁 Generated assets are in the 'assets' directory"
echo ""
echo "Usage examples:"
echo "  HTML: <link rel=\"icon\" href=\"assets/favicon/favicon.ico\">"
echo "  PNG:  <img src=\"assets/png/icon-64x64.png\" width=\"64\">"
echo "  OG:   <meta property=\"og:image\" content=\"assets/opengraph/icon-1200x630.png\">"
