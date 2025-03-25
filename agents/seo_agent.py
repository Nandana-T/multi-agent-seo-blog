# agents/seo_agent.py (updated)
from utils.formatter import Formatter

class SEOAgent:
    def optimize(self, content, keywords):
        formatter = Formatter()
        meta_description = "Explore the latest remote work trends and strategies for 2025."
        optimized = formatter.add_front_matter(
            content, 
            "Remote Work Policies in 2025: Trends and Strategies", 
            keywords, 
            meta_description
        )
        return formatter.format_markdown(optimized)