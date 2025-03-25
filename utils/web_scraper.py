# utils/web_scraper.py
import os
from serpapi import GoogleSearch
import logging

class WebScraper:
    def scrape_web(self, query):  # Changed to scrape_web
        try:
            api_key = os.environ.get("SERPAPI_API_KEY")
            if not api_key:
                raise ValueError("SERPAPI_API_KEY environment variable not set")
            
            params = {
                "engine": "google",
                "q": query,
                "api_key": api_key
            }
            search = GoogleSearch(params)
            results = search.get_dict().get("organic_results", [])
            snippets = [r.get("snippet", "") for r in results[:5]]
            logging.info(f"Scraped {len(snippets)} results for query: {query}")
            return snippets
        except Exception as e:
            logging.error(f"Web scraping failed for query '{query}': {str(e)}")
            return []