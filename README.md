# WordPress to GitHub Pages Backup

A simple, automated solution to backup and sync your WordPress blogs to GitHub Pages as Markdown files.

## Features

- Converts WordPress XML exports to Markdown format
- **Downloads and saves all images locally** (fully self-contained backup)
- Preserves post metadata (title, date, author, categories, tags)
- Converts HTML content to Markdown (headings, links, images, code blocks, etc.)
- Organizes posts by date and pages separately
- Generates an index/archive page automatically
- Automated sync script with Git integration
- Simple Markdown files (no static site generator required)

## Quick Start

### Step 1: Export Your WordPress Content

You have two options:

**Option A: WordPress Dashboard (easiest)**
1. Log in to your WordPress admin dashboard
2. Go to **Tools → Export**
3. Select **All content**
4. Click **Download Export File**
5. Save the XML file to this directory

**Option B: WP-CLI (if you have SSH access)**
```bash
# SSH into your WordPress server
wp export --dir=./ --filename=wordpress-export.xml

# Download the file
scp user@yourserver:/path/to/wordpress-export.xml ./
```

### Step 2: Convert to Markdown

Run the converter script:

```bash
python3 wp_to_markdown.py wordpress-export.xml
```

This will create a `blog/` directory with:
```
blog/
├── README.md          # Auto-generated index/archive
├── images/            # Downloaded images from your posts
│   ├── a1b2c3d4.jpg
│   └── e5f6g7h8.png
├── posts/             # Blog posts organized by date
│   ├── 2024-01-15-my-first-post.md
│   └── 2024-02-20-another-post.md
└── pages/             # WordPress pages
    └── about-me.md
```

The script automatically downloads all images from your WordPress posts and updates the Markdown files to reference the local copies.

### Step 3: Set Up GitHub Repository

```bash
cd blog

# Initialize Git repository
git init

# Create a new repository on GitHub, then:
git remote add origin https://github.com/yourusername/your-blog-backup.git

# Commit and push
git add .
git commit -m "Initial WordPress backup"
git push -u origin main
```

### Step 4: Enable GitHub Pages

1. Go to your GitHub repository settings
2. Navigate to **Pages** section
3. Select **Source**: Deploy from branch
4. Select **Branch**: main, folder: / (root)
5. Click **Save**

Your blog will be available at: `https://yourusername.github.io/your-blog-backup/`

## Automated Sync

For ongoing backups, use the sync script:

### One-Time Setup

```bash
# Optional: Set your WordPress path for automatic exports
export WORDPRESS_PATH="/path/to/wordpress"

# Optional: Configure output directory
export OUTPUT_DIR="./blog"

# Run initial sync
./sync_wordpress.sh
```

### Regular Backups

**Manual sync:**
```bash
./sync_wordpress.sh
```

**Automated sync with cron:**
```bash
# Edit crontab
crontab -e

# Add this line to run daily at 2 AM:
0 2 * * * cd /path/to/wordpress-backup && ./sync_wordpress.sh >> sync.log 2>&1
```

## Usage Examples

### Convert with custom output directory
```bash
python3 wp_to_markdown.py export.xml ./my-backup
```

### Convert without downloading images
```bash
# Keep original WordPress URLs instead of downloading images
python3 wp_to_markdown.py export.xml ./blog --no-images
```

### Sync with custom settings
```bash
OUTPUT_DIR="./backup" GIT_BRANCH="main" ./sync_wordpress.sh
```

### Manual conversion steps
```bash
# 1. Export from WordPress
wp export --filename=export.xml

# 2. Convert to Markdown (with images)
python3 wp_to_markdown.py export.xml ./blog

# 3. Review files
cd blog
ls -la posts/
ls -la images/
cat README.md

# 4. Push to GitHub
git add .
git commit -m "Update blog backup"
git push
```

## Customization

### Modify the Converter

Edit `wp_to_markdown.py` to customize:

- **HTML to Markdown conversion**: Modify the `clean_html()` function
- **Filename format**: Change the `sanitize_filename()` function
- **Front matter**: Edit the `create_markdown_file()` function
- **Index layout**: Modify the `create_index_files()` function

### Modify the Sync Script

Edit `sync_wordpress.sh` to customize:

- Backup schedule and automation
- Git commit messages
- Export location and cleanup behavior
- Pre/post-sync hooks

## Advanced Features

### Incremental Backups

The sync script automatically detects changes and only commits when there are updates:

```bash
# Run sync - only commits if there are changes
./sync_wordpress.sh
```

### Multiple Blogs

Backup multiple WordPress sites:

```bash
# Blog 1
python3 wp_to_markdown.py blog1-export.xml ./blog1
cd blog1 && git init && git remote add origin https://github.com/user/blog1.git && cd ..

# Blog 2
python3 wp_to_markdown.py blog2-export.xml ./blog2
cd blog2 && git init && git remote add origin https://github.com/user/blog2.git && cd ..
```

### Custom CSS for GitHub Pages

Create a custom stylesheet:

```bash
cd blog
cat > style.css <<EOF
body {
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
}
EOF

# Reference in README.md
echo '<link rel="stylesheet" href="style.css">' >> README.md
```

## Troubleshooting

### Issue: XML parsing error
```
Error parsing XML: syntax error
```
**Solution**: Ensure the XML file is complete and valid. Re-export from WordPress.

### Issue: No posts found
```
Found 0 published posts/pages
```
**Solution**: Check that you exported "All content" and that posts are published (not drafts).

### Issue: Images not downloading
```
⚠ Failed to download https://example.com/image.jpg: HTTP Error 403
```
**Solution**: Some WordPress sites block automated downloads. Options:
1. The original URL is kept as fallback - images will still load from WordPress
2. Manually download images and place them in the `blog/images/` directory
3. Use `--no-images` flag to skip image downloading entirely
4. Check your WordPress site's security settings (Cloudflare, WAF, etc.)

### Issue: Image links broken after conversion
**Solution**: Images are saved with relative paths (`../images/filename.jpg`). Ensure you're viewing from the correct directory structure. If using GitHub Pages, the relative paths will work automatically.

### Issue: Special characters in filenames
**Solution**: The converter automatically sanitizes filenames. If you encounter issues, check the `sanitize_filename()` function.

## File Structure

```
wordpress/
├── README.md                  # This file
├── wp_to_markdown.py          # Converter script
├── sync_wordpress.sh          # Automation script
└── blog/                      # Generated output (after conversion)
    ├── README.md              # Blog index/archive
    ├── images/                # Downloaded images
    │   ├── a1b2c3d4.jpg
    │   └── ...
    ├── posts/                 # Blog posts
    │   ├── 2024-01-15-post-title.md
    │   └── ...
    └── pages/                 # WordPress pages
        ├── about.md
        └── ...
```

## Requirements

- Python 3.6+
- Git
- WordPress XML export file

Optional:
- WP-CLI (for automated exports)
- SSH access to WordPress server (for automated exports)

## Security Notes

- **Never commit sensitive data**: Review exported content before pushing
- **Keep WordPress credentials secure**: Don't include them in scripts
- **Use environment variables**: For sensitive configuration like paths
- **Review exports**: Check for private/draft content before making repository public

## Contributing

Feel free to customize these scripts for your needs:

- Add support for custom post types
- Improve HTML to Markdown conversion
- Add support for other media types (videos, PDFs, etc.)
- Implement webhook-based automation
- Create GitHub Actions workflow
- Add progress bars for large exports

## License

MIT License - Feel free to use and modify as needed.

## Additional Resources

- [WordPress Export Documentation](https://wordpress.org/support/article/tools-export-screen/)
- [WP-CLI Export Command](https://developer.wordpress.org/cli/commands/export/)
- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Markdown Guide](https://www.markdownguide.org/)

## Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review the generated files in the `blog/` directory
3. Check conversion logs for errors
4. Verify your WordPress XML export is valid
