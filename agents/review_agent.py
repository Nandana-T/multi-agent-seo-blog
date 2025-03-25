# agents/review_agent.py
class ReviewAgent:
    def review(self, content):
        # Basic proofreading (expand with grammar tools like LanguageTool)
        return content.replace(" .", ".").replace(" ,", ",")