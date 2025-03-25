# Multi-Agent SEO Blog Generator

This project is a Python-based multi-agent system designed to generate a high-quality, SEO-optimized blog post (approximately 2000 words) on the topic "Remote Work Policies in 2025." It leverages multiple agents for research, content planning, generation, SEO optimization, and review, fulfilling the requirements of an HR-related blog generation task.

## Features
- **Multi-Agent Architecture**: Includes Research, Planning, Content Generation, SEO Optimization, and Review agents.
- **SEO Optimization**: Incorporates keywords, meta tags, and structured content for search engine visibility.
- **Content Quality**: Generates a ~2000-word blog post with a clear structure (introduction, sections, conclusion).
- **Hugging Face Integration**: Uses the `mistralai/Mixtral-8x7B-Instruct-v0.1` model for advanced content generation.
- **Output Formats**: Saves the blog as a Markdown file (`output/blog_post.md`).

## Project Structure
```
multi-agent-seo-blog-generator/
├── agents/
│   ├── init.py              # Marks directory as a package
│   ├── research_agent.py        # Collects web data using SerpApi
│   ├── planning_agent.py        # Creates blog outline
│   ├── content_agent.py         # Generates content using Hugging Face
│   ├── seo_agent.py             # Optimizes content for SEO
│   ├── review_agent.py          # Proofreads and refines content
├── utils/                       # (Optional) Utility modules (not implemented yet)
├── output/                      # Generated blog output
│   └── blog_post.md             # Final blog post
├── main.py                      # Main script to run the system
├── app.py                       # Flask app for Vercel deployment (not implemented yet)
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## System Architecture
The system follows a modular, multi-agent workflow:
1. **Research Agent**: Collects trending HR data using SerpApi.
2. **Planning Agent**: Creates a structured blog outline (~2000 words total).
3. **Content Generation Agent**: Writes the blog using Hugging Face's Mixtral model, incorporating research data.
4. **SEO Optimization Agent**: Adds keywords and meta tags for SEO compliance.
5. **Review Agent**: Proofreads and ensures content quality.

## Prerequisites
- **Python 3.9+**
- **SerpApi Key**: For web research (free tier: 100 searches/month).
- **Hugging Face API Token**: For content generation.
- 
## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/multi-agent-seo-blog-generator.git
cd multi-agent-seo-blog-generator
```

### 2. Install Dependencies
Create a virtual environment (optional) and install required packages:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.tx
```
requirements.txt contents:
```text
transformers==4.35.0
torch==2.0.1
huggingface_hub
requests==2.28.1
python-dotenv==1.0.1
```

### 3. Set Up API Keys
SerpApi Key:
    1. Sign up at serpapi.com (free tier: 100 searches/month).
    2. Copy your API key.
    3. Set it in your environment:
  ```bash
export SERPAPI_KEY="your_serpapi_key"
```
Hugging Face Token:
    1. Log in to huggingface.co, go to Settings → Access Tokens.
    2. Create/copy your token.
    3. Set it in your environment:
  ```bash
export HF_TOKEN="hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```
Alternatively, use a .env file in the project root:
```text
SERPAPI_KEY=your_serpapi_key
HF_TOKEN=hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```
Then install python-dotenv (already in requirements.txt) and ensure load_dotenv() is used in your agents.

### 4. Run the Application
```bash
python main.py
```
The script will generate a blog post and save it to output/blog_post.md.

