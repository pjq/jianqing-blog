# WordPress to GitHub Pages Backup

A simple, automated solution to backup and sync your WordPress blogs to GitHub Pages as Markdown files.

## 🌐 Live Site

**View the archive:** [https://github.pjq.me/jianqing-blog/](https://github.pjq.me/jianqing-blog/)

## Features

- Converts WordPress XML exports to Markdown format
- **Downloads and saves all images locally** (fully self-contained backup)
- Preserves post metadata (title, date, author, categories, tags)
- Converts HTML content to Markdown (headings, links, images, code blocks, etc.)
- Organizes posts by date and pages separately
- Generates an index/archive page automatically
- Automated sync script with Git integration
- **Jekyll-ready for GitHub Pages** with automatic Markdown rendering

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

### Step 3: Set Up Jekyll for GitHub Pages

For proper Markdown rendering on GitHub Pages, you need to set up Jekyll:

```bash
# Create docs directory for GitHub Pages
mkdir -p docs

# Copy converted content to docs
cp -r blog/posts docs/_posts
cp -r blog/images docs/images

# Create Jekyll configuration
cat > docs/_config.yml <<EOF
title: Your Blog Archive
description: WordPress backup from yourblog.com (2007-2025)
url: https://yourusername.github.io
baseurl: /your-blog-backup

markdown: kramdown
kramdown:
  input: GFM
  syntax_highlighter: rouge

collections:
  posts:
    output: true
    permalink: /posts/:title/

theme: minima
plugins:
  - jekyll-feed
  - jekyll-seo-tag
EOF

# Create layout templates
mkdir -p docs/_layouts

# Create default layout
cat > docs/_layouts/default.html <<'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page.title }} - Your Blog</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            line-height: 1.6;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }
        header {
            border-bottom: 2px solid #667eea;
            margin-bottom: 30px;
        }
        header h1 a {
            color: #667eea;
            text-decoration: none;
        }
        .content img {
            max-width: 100%;
            height: auto;
        }
    </style>
</head>
<body>
    <header>
        <h1><a href="{{ site.baseurl }}/">Your Blog Archive</a></h1>
        <nav>
            <a href="{{ site.baseurl }}/">Home</a>
            <a href="{{ site.baseurl }}/blog-index.html">All Posts</a>
        </nav>
    </header>
    <main>{{ content }}</main>
</body>
</html>
EOF

# Create post layout
cat > docs/_layouts/post.html <<'EOF'
---
layout: default
---
<article class="post">
    <h1>{{ page.title }}</h1>
    <div class="post-meta">
        <time>{{ page.date | date: "%B %d, %Y" }}</time>
        {% if page.author %} • By {{ page.author }}{% endif %}
    </div>
    <div class="content">{{ content }}</div>
</article>
EOF

# Create homepage
cat > docs/index.md <<'EOF'
---
layout: default
title: Home
---

# Your Blog Archive

Welcome to the complete archive of your WordPress blog!

## Recent Posts

<ul>
{% for post in site.posts limit:10 %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <span style="color: #999;">({{ post.date | date: "%Y-%m-%d" }})</span>
  </li>
{% endfor %}
</ul>

[View all posts →](blog-index.html)
EOF
```

### Step 4: Set Up GitHub Repository

```bash
# Initialize Git repository at the root
git init

# Create a new repository on GitHub, then:
git remote add origin https://github.com/yourusername/your-blog-backup.git

# Commit and push
git add .
git commit -m "Initial WordPress backup with Jekyll"
git push -u origin main
```

### Step 5: Enable GitHub Pages

1. Go to your GitHub repository settings
2. Navigate to **Pages** section
3. Select **Source**: Deploy from branch
4. Select **Branch**: main, **folder**: /docs
5. Click **Save**

Your blog will be available at: `https://yourusername.github.io/your-blog-backup/`

**Important**: GitHub Pages will automatically build the Jekyll site. All Markdown files in `docs/_posts/` will be converted to HTML and served at clean URLs (e.g., `/posts/my-post-title/` instead of `/posts/my-post-title.md`).

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

### Issue: Markdown files return 404 on GitHub Pages
```
https://yourusername.github.io/blog/posts/my-post.md returns 404
```
**Solution**: GitHub Pages only serves HTML files, not raw Markdown. You need to set up Jekyll:
1. Follow the Jekyll setup instructions in Step 3 above
2. Ensure posts are in `docs/_posts/` directory (not `docs/posts/`)
3. GitHub Pages will automatically build Jekyll and serve posts at clean URLs like `/posts/my-post/` (without .md extension)
4. Wait a few minutes after pushing for GitHub Pages to rebuild the site

## File Structure

```
wordpress-backup/
├── README.md                  # This file
├── wp_to_markdown.py          # Converter script
├── sync_wordpress.sh          # Automation script
├── blog/                      # Generated output (after conversion)
│   ├── README.md              # Blog index/archive
│   ├── images/                # Downloaded images
│   │   ├── a1b2c3d4.jpg
│   │   └── ...
│   ├── posts/                 # Blog posts (before Jekyll setup)
│   │   ├── 2024-01-15-post-title.md
│   │   └── ...
│   └── pages/                 # WordPress pages
│       ├── about.md
│       └── ...
└── docs/                      # Jekyll site for GitHub Pages
    ├── _config.yml            # Jekyll configuration
    ├── _layouts/              # Jekyll layout templates
    │   ├── default.html
    │   └── post.html
    ├── _posts/                # Blog posts (Jekyll format)
    │   ├── 2024-01-15-post-title.md
    │   └── ...
    ├── images/                # Images (copied from blog/)
    │   ├── a1b2c3d4.jpg
    │   └── ...
    ├── index.md               # Homepage
    └── blog-index.html        # All posts index
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
