#!/bin/bash
# WordPress to GitHub Pages Sync Script
# Automates the backup of WordPress content to GitHub

set -e  # Exit on error

# Configuration
WORDPRESS_PATH="${WORDPRESS_PATH:-}"
EXPORT_FILE="wordpress-export-$(date +%Y%m%d-%H%M%S).xml"
OUTPUT_DIR="${OUTPUT_DIR:-./blog}"
GIT_BRANCH="${GIT_BRANCH:-main}"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${GREEN}→${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}⚠${NC} $1"
}

log_error() {
    echo -e "${RED}✗${NC} $1"
}

check_dependencies() {
    log_info "Checking dependencies..."

    if ! command -v python3 &> /dev/null; then
        log_error "python3 is required but not installed"
        exit 1
    fi

    if ! command -v git &> /dev/null; then
        log_error "git is required but not installed"
        exit 1
    fi

    log_info "All dependencies found"
}

export_wordpress() {
    log_info "Exporting WordPress content..."

    if [ -n "$WORDPRESS_PATH" ] && command -v wp &> /dev/null; then
        # Use WP-CLI if available and path is set
        log_info "Using WP-CLI to export..."
        cd "$WORDPRESS_PATH"
        wp export --path="$WORDPRESS_PATH" --dir="$OLDPWD" --filename="$EXPORT_FILE"
        cd - > /dev/null
    else
        log_warn "WP-CLI not available or WORDPRESS_PATH not set"
        echo ""
        echo "Please export your WordPress content manually:"
        echo "  1. Go to WordPress Dashboard → Tools → Export"
        echo "  2. Select 'All content' and download the XML file"
        echo "  3. Save it in this directory as: $EXPORT_FILE"
        echo ""
        read -p "Press Enter when you've saved the export file, or Ctrl+C to cancel..."

        if [ ! -f "$EXPORT_FILE" ]; then
            log_error "Export file not found: $EXPORT_FILE"
            exit 1
        fi
    fi

    log_info "Export file ready: $EXPORT_FILE"
}

convert_to_markdown() {
    log_info "Converting WordPress content to Markdown..."

    python3 wp_to_markdown.py "$EXPORT_FILE" "$OUTPUT_DIR"

    if [ $? -eq 0 ]; then
        log_info "Conversion completed successfully"
    else
        log_error "Conversion failed"
        exit 1
    fi
}

setup_git_repo() {
    log_info "Setting up Git repository..."

    cd "$OUTPUT_DIR"

    if [ ! -d .git ]; then
        log_info "Initializing Git repository..."
        git init

        # Create .gitignore
        cat > .gitignore <<EOF
# System files
.DS_Store
Thumbs.db

# Temporary files
*.tmp
*.bak
*~
EOF
    fi

    # Check for changes
    if [ -z "$(git status --porcelain)" ]; then
        log_warn "No changes to commit"
        cd - > /dev/null
        return
    fi

    # Stage all changes
    git add .

    # Commit with timestamp
    COMMIT_MSG="Sync WordPress backup - $(date '+%Y-%m-%d %H:%M:%S')"
    git commit -m "$COMMIT_MSG"

    log_info "Changes committed: $COMMIT_MSG"

    # Check if remote is configured
    if git remote | grep -q origin; then
        log_info "Pushing to GitHub..."
        git push origin "$GIT_BRANCH"
        log_info "Pushed to GitHub successfully"
    else
        log_warn "No remote repository configured"
        echo ""
        echo "To push to GitHub:"
        echo "  1. Create a new repository on GitHub"
        echo "  2. Run: git remote add origin https://github.com/username/repo.git"
        echo "  3. Run: git push -u origin $GIT_BRANCH"
        echo "  4. Enable GitHub Pages in repository settings"
    fi

    cd - > /dev/null
}

cleanup() {
    if [ -f "$EXPORT_FILE" ]; then
        log_info "Cleaning up export file..."
        rm "$EXPORT_FILE"
    fi
}

main() {
    echo "WordPress to GitHub Pages Sync"
    echo "================================"
    echo ""

    check_dependencies
    export_wordpress
    convert_to_markdown
    setup_git_repo
    cleanup

    echo ""
    log_info "Sync complete!"
    echo ""
    echo "Your WordPress content has been backed up to: $OUTPUT_DIR"
    echo "View the index at: $OUTPUT_DIR/README.md"
}

# Run main function
main
