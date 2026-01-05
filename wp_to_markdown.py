#!/usr/bin/env python3
"""
WordPress to Markdown Converter
Converts WordPress XML export to Markdown files for GitHub Pages
"""

try:
    from lxml import etree as ET
    LXML_AVAILABLE = True
except ImportError:
    import xml.etree.ElementTree as ET
    LXML_AVAILABLE = False

import re
import os
import sys
from datetime import datetime
from pathlib import Path
import html
import urllib.parse
import urllib.request
import hashlib
from urllib.error import URLError, HTTPError


def extract_images(content):
    """Extract all image URLs from HTML content"""
    if not content:
        return []

    images = []

    # Find img tags with src
    img_pattern = r'<img[^>]*src=["\']([^"\']*)["\'][^>]*>'
    matches = re.findall(img_pattern, content, flags=re.IGNORECASE)

    for url in matches:
        if url and not url.startswith('data:'):  # Skip data URLs
            images.append(url)

    return images


def download_image(url, output_dir, downloaded_images):
    """Download an image and return the local path"""
    try:
        # Check if already downloaded
        if url in downloaded_images:
            return downloaded_images[url]

        # Create images directory
        images_dir = output_dir / 'images'
        images_dir.mkdir(parents=True, exist_ok=True)

        # Generate a unique filename based on URL
        parsed_url = urllib.parse.urlparse(url)
        original_filename = os.path.basename(parsed_url.path)

        # If no extension, try to get from URL
        if '.' not in original_filename:
            original_filename = 'image.jpg'

        # Create hash of URL to avoid duplicates and long filenames
        url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
        ext = os.path.splitext(original_filename)[1] or '.jpg'
        filename = f"{url_hash}{ext}"

        local_path = images_dir / filename

        # Download if not already exists
        if not local_path.exists():
            print(f"    Downloading image: {url}")

            # Set user agent to avoid blocks
            req = urllib.request.Request(
                url,
                headers={'User-Agent': 'Mozilla/5.0 (compatible; WordPress Backup Bot)'}
            )

            with urllib.request.urlopen(req, timeout=10) as response:
                with open(local_path, 'wb') as f:
                    f.write(response.read())

        # Store relative path from post directory
        relative_path = f"../images/{filename}"
        downloaded_images[url] = relative_path

        return relative_path

    except (URLError, HTTPError, Exception) as e:
        print(f"    ⚠ Failed to download {url}: {e}")
        return url  # Return original URL as fallback


def clean_html(content, output_dir=None, download_images_flag=True):
    """Convert HTML content to Markdown-like format"""
    if not content:
        return ""

    # Track downloaded images
    downloaded_images = {}

    # Download images if requested
    if download_images_flag and output_dir:
        image_urls = extract_images(content)
        for url in image_urls:
            local_path = download_image(url, output_dir, downloaded_images)
            # Replace URL in content
            if local_path != url:
                content = content.replace(url, local_path)

    # Unescape HTML entities
    content = html.unescape(content)

    # Convert common HTML tags to Markdown
    conversions = [
        (r'<h1[^>]*>(.*?)</h1>', r'# \1\n'),
        (r'<h2[^>]*>(.*?)</h2>', r'## \1\n'),
        (r'<h3[^>]*>(.*?)</h3>', r'### \1\n'),
        (r'<h4[^>]*>(.*?)</h4>', r'#### \1\n'),
        (r'<h5[^>]*>(.*?)</h5>', r'##### \1\n'),
        (r'<h6[^>]*>(.*?)</h6>', r'###### \1\n'),
        (r'<strong>(.*?)</strong>', r'**\1**'),
        (r'<b>(.*?)</b>', r'**\1**'),
        (r'<em>(.*?)</em>', r'*\1*'),
        (r'<i>(.*?)</i>', r'*\1*'),
        (r'<code>(.*?)</code>', r'`\1`'),
        (r'<pre[^>]*>(.*?)</pre>', r'```\n\1\n```\n'),
        (r'<a[^>]*href=["\']([^"\']*)["\'][^>]*>(.*?)</a>', r'[\2](\1)'),
        (r'<img[^>]*src=["\']([^"\']*)["\'][^>]*alt=["\']([^"\']*)["\'][^>]*>', r'![\2](\1)'),
        (r'<img[^>]*src=["\']([^"\']*)["\'][^>]*>', r'![](\1)'),
        (r'<br\s*/?>', '\n'),
        (r'<p[^>]*>', '\n'),
        (r'</p>', '\n'),
        (r'<ul[^>]*>', '\n'),
        (r'</ul>', '\n'),
        (r'<ol[^>]*>', '\n'),
        (r'</ol>', '\n'),
        (r'<li[^>]*>', '- '),
        (r'</li>', '\n'),
        (r'<blockquote[^>]*>', '\n> '),
        (r'</blockquote>', '\n'),
    ]

    for pattern, replacement in conversions:
        content = re.sub(pattern, replacement, content, flags=re.DOTALL | re.IGNORECASE)

    # Remove remaining HTML tags
    content = re.sub(r'<[^>]+>', '', content)

    # Clean up excessive newlines
    content = re.sub(r'\n{3,}', '\n\n', content)

    return content.strip()


def sanitize_filename(title):
    """Convert title to safe filename"""
    # Remove special characters
    filename = re.sub(r'[^\w\s-]', '', title.lower())
    # Replace spaces with hyphens
    filename = re.sub(r'[-\s]+', '-', filename)
    return filename[:100]  # Limit length


def parse_wordpress_xml_regex_fallback(xml_content):
    """Parse posts using regex as fallback for items lxml can't parse"""
    posts = []

    # Find all <item>...</item> blocks
    items = re.findall(r'<item>(.*?)</item>', xml_content, re.DOTALL)

    for item_content in items:
        # Check if it's a published post
        if '<wp:post_type><![CDATA[post]]></wp:post_type>' not in item_content:
            continue
        if '<wp:status><![CDATA[publish]]></wp:status>' not in item_content:
            continue

        # Extract fields using regex
        title_match = re.search(r'<title><!\[CDATA\[(.*?)\]\]></title>', item_content)
        content_match = re.search(r'<content:encoded><!\[CDATA\[(.*?)\]\]></content:encoded>', item_content, re.DOTALL)
        date_match = re.search(r'<wp:post_date><!\[CDATA\[(.*?)\]\]></wp:post_date>', item_content)
        author_match = re.search(r'<dc:creator><!\[CDATA\[(.*?)\]\]></dc:creator>', item_content)

        title = title_match.group(1) if title_match else 'Untitled'
        content = content_match.group(1) if content_match else ''
        date = date_match.group(1) if date_match else ''
        author = author_match.group(1) if author_match else 'Unknown'

        # Extract categories and tags
        categories = re.findall(r'<category domain="category"[^>]*><!\[CDATA\[(.*?)\]\]></category>', item_content)
        tags = re.findall(r'<category domain="post_tag"[^>]*><!\[CDATA\[(.*?)\]\]></category>', item_content)

        posts.append({
            'title': title,
            'content': content,
            'date': date,
            'author': author,
            'categories': categories,
            'tags': tags,
            'type': 'post'
        })

    return posts


def parse_wordpress_xml(xml_file):
    """Parse WordPress XML export file"""
    try:
        # Use lxml with recovery mode if available, otherwise use standard parser
        if LXML_AVAILABLE:
            parser = ET.XMLParser(recover=True, encoding='utf-8', huge_tree=True)
            tree = ET.parse(xml_file, parser=parser)
        else:
            tree = ET.parse(xml_file)
        root = tree.getroot()

        # WordPress XML uses namespaces
        namespaces = {
            'content': 'http://purl.org/rss/1.0/modules/content/',
            'wp': 'http://wordpress.org/export/1.2/',
            'dc': 'http://purl.org/dc/elements/1.1/',
        }

        posts = []

        print(f"Total items found by XML parser: {len(root.findall('.//item'))}")

        for item in root.findall('.//item'):
            post_type = item.find('wp:post_type', namespaces)

            # Only process posts and pages
            if post_type is not None and post_type.text in ['post', 'page']:
                status = item.find('wp:status', namespaces)

                # Only process published content
                if status is not None and status.text == 'publish':
                    title_elem = item.find('title')
                    content_elem = item.find('content:encoded', namespaces)
                    date_elem = item.find('wp:post_date', namespaces)
                    author_elem = item.find('dc:creator', namespaces)

                    title = title_elem.text if title_elem is not None else 'Untitled'
                    content = content_elem.text if content_elem is not None else ''
                    date = date_elem.text if date_elem is not None else ''
                    author = author_elem.text if author_elem is not None else 'Unknown'

                    # Extract categories and tags
                    categories = []
                    tags = []
                    for category in item.findall('category'):
                        domain = category.get('domain')
                        if domain == 'category':
                            categories.append(category.text)
                        elif domain == 'post_tag':
                            tags.append(category.text)

                    posts.append({
                        'title': title,
                        'content': content,
                        'date': date,
                        'author': author,
                        'categories': categories,
                        'tags': tags,
                        'type': post_type.text
                    })

        # Use regex fallback to find missing posts
        print(f"Found {len(posts)} posts with XML parser")
        print("Checking for missing posts with regex fallback...")

        with open(xml_file, 'r', encoding='utf-8') as f:
            xml_content = f.read()

        regex_posts = parse_wordpress_xml_regex_fallback(xml_content)
        print(f"Found {len(regex_posts)} posts with regex parser")

        # Find posts in regex but not in XML parser (by title)
        xml_titles = {p['title'] for p in posts}
        missing_posts = [p for p in regex_posts if p['title'] not in xml_titles]

        if missing_posts:
            print(f"\nFound {len(missing_posts)} additional posts missed by XML parser:")
            for p in missing_posts:
                print(f"  - {p['title']} ({p['date'][:10]})")
            posts.extend(missing_posts)
        else:
            print("No additional posts found.")

        return posts

    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        sys.exit(1)


def create_markdown_file(post, output_dir, download_images_flag=True):
    """Create a Markdown file from a WordPress post"""
    # Parse date
    try:
        date_obj = datetime.strptime(post['date'], '%Y-%m-%d %H:%M:%S')
        date_str = date_obj.strftime('%Y-%m-%d')
    except:
        date_str = datetime.now().strftime('%Y-%m-%d')

    # Create filename
    filename = f"{date_str}-{sanitize_filename(post['title'])}.md"

    # Determine output path based on post type
    if post['type'] == 'page':
        type_dir = output_dir / 'pages'
    else:
        type_dir = output_dir / 'posts'

    type_dir.mkdir(parents=True, exist_ok=True)
    filepath = type_dir / filename

    # Create front matter
    front_matter = [
        '---',
        f"title: \"{post['title']}\"",
        f"date: {date_str}",
        f"author: {post['author']}",
    ]

    if post['categories']:
        front_matter.append(f"categories: {post['categories']}")

    if post['tags']:
        front_matter.append(f"tags: {post['tags']}")

    front_matter.append('---')
    front_matter.append('')

    # Convert content (with image downloading if enabled)
    markdown_content = clean_html(post['content'], output_dir, download_images_flag)

    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(front_matter))
        f.write('\n')
        f.write(markdown_content)

    return filepath


def create_index_files(output_dir, posts):
    """Create index files for navigation"""
    # Create main index
    index_content = ['# Blog Archive\n']

    # Group posts by year
    posts_by_year = {}
    pages = []

    for post in posts:
        if post['type'] == 'page':
            pages.append(post)
        else:
            try:
                date_obj = datetime.strptime(post['date'], '%Y-%m-%d %H:%M:%S')
                year = date_obj.year
                if year not in posts_by_year:
                    posts_by_year[year] = []
                posts_by_year[year].append(post)
            except:
                pass

    # Add pages section
    if pages:
        index_content.append('## Pages\n')
        for page in pages:
            filename = f"{sanitize_filename(page['title'])}.md"
            index_content.append(f"- [{page['title']}](pages/{filename})")
        index_content.append('')

    # Add posts by year
    index_content.append('## Posts\n')
    for year in sorted(posts_by_year.keys(), reverse=True):
        index_content.append(f'### {year}\n')
        for post in sorted(posts_by_year[year], key=lambda x: x['date'], reverse=True):
            try:
                date_obj = datetime.strptime(post['date'], '%Y-%m-%d %H:%M:%S')
                date_str = date_obj.strftime('%Y-%m-%d')
                filename = f"{date_str}-{sanitize_filename(post['title'])}.md"
                index_content.append(f"- [{post['title']}](posts/{filename}) - {date_str}")
            except:
                pass
        index_content.append('')

    # Write main index
    with open(output_dir / 'README.md', 'w', encoding='utf-8') as f:
        f.write('\n'.join(index_content))


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 wp_to_markdown.py <wordpress-export.xml> [output-directory] [--no-images]")
        print("\nTo export from WordPress:")
        print("  1. Dashboard → Tools → Export → All content")
        print("  2. Or use WP-CLI: wp export --dir=./")
        print("\nOptions:")
        print("  --no-images    Skip downloading images (keep original URLs)")
        sys.exit(1)

    # Parse arguments
    xml_file = sys.argv[1]
    download_images_flag = '--no-images' not in sys.argv

    # Get output directory (skip --no-images if present)
    output_dir = './blog'
    for i, arg in enumerate(sys.argv[2:], start=2):
        if not arg.startswith('--'):
            output_dir = arg
            break

    output_dir = Path(output_dir)

    if not os.path.exists(xml_file):
        print(f"Error: File '{xml_file}' not found")
        sys.exit(1)

    print(f"Parsing WordPress export: {xml_file}")
    print(f"Download images: {'Yes' if download_images_flag else 'No'}")
    posts = parse_wordpress_xml(xml_file)

    print(f"Found {len(posts)} published posts/pages")

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Convert each post
    print(f"\nConverting to Markdown...")
    for i, post in enumerate(posts, 1):
        print(f"  [{i}/{len(posts)}] {post['title']}")
        filepath = create_markdown_file(post, output_dir, download_images_flag)
        print(f"    → {filepath}")

    # Create index files
    print("\nCreating index files...")
    create_index_files(output_dir, posts)

    print(f"\n✓ Conversion complete!")
    print(f"  Output directory: {output_dir.absolute()}")
    print(f"  Posts: {output_dir / 'posts'}")
    print(f"  Pages: {output_dir / 'pages'}")
    if download_images_flag:
        print(f"  Images: {output_dir / 'images'}")
    print(f"  Index: {output_dir / 'README.md'}")
    print(f"\nNext steps:")
    print(f"  1. Review the converted files in '{output_dir}'")
    print(f"  2. Initialize git: cd {output_dir} && git init")
    print(f"  3. Create GitHub repo and push")
    print(f"  4. Enable GitHub Pages in repo settings")


if __name__ == '__main__':
    main()
