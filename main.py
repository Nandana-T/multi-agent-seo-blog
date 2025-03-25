# main.py
from agents.research_agent import ResearchAgent
from agents.content_agent import ContentAgent
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class BlogGenerator:
    def __init__(self):
        self.research_agent = ResearchAgent()
        self.content_agent = ContentAgent()

    def generate_blog(self):
        logging.info("Starting research phase...")
        research_data = self.research_agent.collect_data(topic_area="HR")
        logging.info(f"Research completed: {len(research_data['web_content'])} web snippets collected")

        logging.info("Generating blog content...")
        final_content = self.content_agent.write_content(None, research_data)
        final_words = len(final_content.split())
        logging.info(f"Content generated: {final_words} words")

        output_path = "output/blog_post.md"
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(final_content)
        logging.info(f"Blog post saved to {output_path}")

        return final_content

if __name__ == "__main__":
    generator = BlogGenerator()
    try:
        blog = generator.generate_blog()
        print("Blog post generated successfully!")
    except Exception as e:
        logging.error(f"Error generating blog: {str(e)}")
        print(f"Failed to generate blog post: {str(e)}")