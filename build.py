#!/usr/bin/env python3
"""
PlayBeat Digital — Build & Package Script
Generates all HTML files, creates dist folder, and packages into ZIP
Usage: python3 build.py
"""

import os
import sys
import shutil
import zipfile
from pathlib import Path
from datetime import datetime

# Colors for terminal output
class Colors:
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    END = '\033[0m'

def log(message, color=Colors.BLUE):
    """Print colored log message"""
    print(f"{color}{message}{Colors.END}")

def log_success(message):
    """Print success message"""
    print(f"{Colors.GREEN}✓ {message}{Colors.END}")

def log_error(message):
    """Print error message"""
    print(f"{Colors.RED}✗ {message}{Colors.END}")

def log_warning(message):
    """Print warning message"""
    print(f"{Colors.YELLOW}⚠ {message}{Colors.END}")

def main():
    log(f"\n{'='*70}", Colors.BOLD)
    log("PlayBeat Digital — Build & Package Script", Colors.BOLD)
    log(f"{'='*70}\n", Colors.BOLD)
    
    # Check if playbeat.py exists
    if not os.path.exists('playbeat.py'):
        log_error("playbeat.py not found in current directory")
        sys.exit(1)
    
    log("Step 1: Importing site generator...", Colors.BLUE)
    try:
        import playbeat
        log_success("Site generator imported")
    except Exception as e:
        log_error(f"Failed to import playbeat.py: {e}")
        sys.exit(1)
    
    # Clean existing dist folder
    log("\nStep 2: Preparing dist directory...", Colors.BLUE)
    dist_path = Path('dist')
    if dist_path.exists():
        log_warning("Removing existing dist folder...")
        shutil.rmtree(dist_path)
    
    dist_path.mkdir(exist_ok=True)
    log_success("dist directory created")
    
    # Copy shared assets
    log("\nStep 3: Copying shared assets...", Colors.BLUE)
    assets_copied = 0
    for asset_file in ['shared.css', 'shared.js']:
        src = Path(asset_file)
        if src.exists():
            shutil.copy(src, dist_path / asset_file)
            log_success(f"Copied {asset_file}")
            assets_copied += 1
        else:
            log_warning(f"{asset_file} not found (optional)")
    
    if assets_copied == 0:
        log_warning("No shared assets found - HTML files may need manual asset configuration")
    
    # Generate HTML pages
    log("\nStep 4: Generating HTML pages...", Colors.BLUE)
    try:
        # Import the pages dictionary from playbeat.py
        from playbeat import pages
        
        pages_created = 0
        for filename, content in pages.items():
            filepath = dist_path / filename
            filepath.write_text(content, encoding='utf-8')
            pages_created += 1
            print(f"  ✓ {filename}")
        
        log_success(f"Generated {pages_created} HTML pages")
    except Exception as e:
        log_error(f"Failed to generate pages: {e}")
        sys.exit(1)
    
    # Create ZIP package
    log("\nStep 5: Creating deployment package...", Colors.BLUE)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    zip_filename = f'PlayBeat_Digital_Package_{timestamp}.zip'
    zip_path = Path(zip_filename)
    
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in dist_path.rglob('*'):
                if file_path.is_file():
                    arcname = file_path.relative_to(dist_path)
                    zipf.write(file_path, arcname)
        
        zip_size = zip_path.stat().st_size / (1024 * 1024)  # Size in MB
        log_success(f"Created {zip_filename} ({zip_size:.2f} MB)")
    except Exception as e:
        log_error(f"Failed to create ZIP: {e}")
        sys.exit(1)
    
    # Generate summary report
    log("\nStep 6: Generating build report...", Colors.BLUE)
    report_path = dist_path / 'BUILD_REPORT.md'
    
    file_count = len(list(dist_path.glob('*')))
    html_count = len(list(dist_path.glob('*.html')))
    
    report = f"""# PlayBeat Digital — Build Report

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Summary
- **Total Files:** {file_count}
- **HTML Pages:** {html_count}
- **Distribution Package:** {zip_filename}
- **Package Size:** {zip_size:.2f} MB

## Files Generated

### HTML Pages ({html_count})
"""
    
    for html_file in sorted(dist_path.glob('*.html')):
        report += f"- {html_file.name}\n"
    
    report += f"""
### Assets
- shared.css (Main stylesheet)
- shared.js (Main JavaScript)

## Directory Structure

```
dist/
├── index.html
├── games.html
├── gift-cards.html
├── software.html
├── ai-tools.html
├── game-items.html
├── accounts.html
├── subscriptions.html
├── top-up.html
├── trending.html
├── best-value.html
├── outsource.html
├── our-team.html
├── faq.html
├── contact.html
├── my-account.html
├── privacy.html
├── terms.html
├── refund.html
├── shared.css
├── shared.js
└── BUILD_REPORT.md
```

## Deployment Instructions

### Local Testing
1. Open `dist/index.html` in your browser
2. Test all navigation and features
3. Verify responsive design on mobile

### Production Deployment

#### Option 1: GitHub Pages
```bash
# Copy dist/ contents to gh-pages branch
git checkout gh-pages
cp -r dist/* .
git add .
git commit -m "Update site $(date +%Y-%m-%d)"
git push origin gh-pages
```

#### Option 2: Netlify
```bash
# Deploy dist/ folder
netlify deploy --prod --dir=dist
```

#### Option 3: Vercel
```bash
# Deploy dist/ folder
vercel --prod
```

#### Option 4: Static Hosting (AWS S3, Cloudflare, etc.)
```bash
# Upload contents of dist/ folder to your hosting
aws s3 sync dist/ s3://your-bucket/
```

## Features

✓ 19 fully responsive pages
✓ Dark theme with gradient accents
✓ Complete e-commerce functionality
✓ User authentication system
✓ Product filtering and search
✓ Shopping cart & checkout
✓ Wishlist management
✓ Order tracking
✓ Account dashboard
✓ FAQ & Contact forms
✓ Privacy & Terms pages
✓ Mobile optimized
✓ Modern animations
✓ Instant delivery simulation

## File Sizes

"""
    
    for file_path in sorted(dist_path.glob('*')):
        if file_path.is_file():
            size = file_path.stat().st_size / 1024  # Size in KB
            report += f"- {file_path.name}: {size:.2f} KB\n"
    
    report += f"""
## Build Script Information

This report was generated by `build.py` using `playbeat.py`.

To rebuild the site:
```bash
python3 build.py
```

To run the site generator directly:
```bash
python3 playbeat.py
```

---
**PlayBeat Digital** — Prime Digital Marketplace Generator
"""
    
    report_path.write_text(report, encoding='utf-8')
    log_success("Build report created (BUILD_REPORT.md)")
    
    # Final summary
    log(f"\n{'='*70}", Colors.BOLD)
    log("BUILD COMPLETE ✓", Colors.GREEN + Colors.BOLD)
    log(f"{'='*70}\n", Colors.BOLD)
    
    print(f"{Colors.GREEN}📦 Package Ready:{Colors.END}")
    print(f"   Location: {zip_filename}")
    print(f"   Size: {zip_size:.2f} MB")
    print(f"   Files: {html_count} HTML pages + assets")
    
    print(f"\n{Colors.BLUE}📁 Build Output:{Colors.END}")
    print(f"   Location: dist/")
    print(f"   Files: {file_count} total files")
    
    print(f"\n{Colors.YELLOW}🚀 Next Steps:{Colors.END}")
    print(f"   1. Test: Open dist/index.html in browser")
    print(f"   2. Review: Check BUILD_REPORT.md in dist/")
    print(f"   3. Deploy: Use {zip_filename} for production")
    print(f"   4. Update: Run build.py after code changes\n")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        log_error("\nBuild cancelled by user")
        sys.exit(1)
    except Exception as e:
        log_error(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
