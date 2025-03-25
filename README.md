# Multi-Agent SEO Blog Generator

This project generates an SEO-optimized blog post about "Remote Work Policies in 2025" using a multi-agent system. It includes agents for research, content generation, SEO optimization, and review.

## Project Structure

- `agents/`: Contains agent classes for research, planning, content generation, SEO, and review.
- `utils/`: Utility modules for web scraping and formatting.
- `main.py`: Orchestrates the blog generation process.
- `app.py`: Flask app for serving the blog on Vercel.
- `output/`: Stores the generated blog post (`blog_post.md`).

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt