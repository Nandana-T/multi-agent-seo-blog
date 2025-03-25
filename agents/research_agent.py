# agents/research_agent.py
from utils.web_scraper import WebScraper
import logging

class ResearchAgent:
    def collect_data(self, topic_area):
        scraper = WebScraper()
        logging.info(f"Scraping web for {topic_area} trends 2025")
        web_data = scraper.scrape_web(f"{topic_area} trends 2025")  # Use scrape, not scrape_web
        x_posts = self.search_x(f"{topic_area} trends")
        trending_topic = "Remote Work Policies in 2025"
        keywords = ["remote work", "hybrid policies", "employee retention"]
        return {
            "topic": trending_topic,
            "keywords": keywords,
            "web_content": web_data,
            "x_insights": x_posts
        }
    
    def search_x(self, query):
        return [
            f"Sample X post about {query}",
            f"Another post discussing {query}"
        ]