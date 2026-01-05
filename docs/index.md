---
layout: default
title: Home
---

# Jianqing's Blog Archive

Welcome to the complete archive of my WordPress blog from [pjq.me](https://pjq.me), spanning from 2007 to 2025.

## Stats

- **316 blog posts** converted to Markdown
- **145 images** downloaded and stored locally
- **18 years** of content (2007-2025)

## Browse Posts

- [View all posts by date](blog-index.html)
- [Visit main blog (pjq.me)](https://pjq.me)
- [View on GitHub](https://github.com/pjq/jianqing-blog)

## Recent Posts

<ul>
{% for post in site.posts limit:10 %}
  <li>
    <a href="{{ post.url | relative_url }}">{{ post.title }}</a>
    <span style="color: #999; font-size: 0.9em;">({{ post.date | date: "%Y-%m-%d" }})</span>
  </li>
{% endfor %}
</ul>

[View all posts →](blog-index.html)
