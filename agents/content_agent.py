# agents/content_agent.py
from huggingface_hub import InferenceClient
import logging
import time
from collections import Counter
import os

class ContentAgent:
    def __init__(self):
        """Initialize the ContentAgent with the Hugging Face InferenceClient."""
        # Retrieve API token from environment variable
        api_token = os.getenv("HF_TOKEN")
        if not api_token:
            raise ValueError("HF_TOKEN environment variable is not set. Please set it with your Hugging Face API token.")
        # Initialize the InferenceClient
        self.client = InferenceClient(token=api_token)
        # Use a more reliable model
        self.model_id = "mistralai/Mixtral-8x7B-Instruct-v0.1"

    def deduplicate_text(self, text, max_repeats=1):
        """Remove duplicate sentences from the text to ensure uniqueness."""
        sentences = [s.strip() for s in text.split(". ") if s.strip()]
        seen = Counter()
        unique_sentences = []
        for sentence in sentences:
            if seen[sentence] < max_repeats:
                unique_sentences.append(sentence)
                seen[sentence] += 1
        return ". ".join(unique_sentences).strip() + "."

    def generate_section(self, instruction, target_words):
        """Generate a section of text up to the target word count using the model."""
        generated_text = ""
        seen_phrases = set()
        max_retries = 3

        while len(generated_text.split()) < target_words:
            for attempt in range(max_retries):
                try:
                    remaining_words = target_words - len(generated_text.split())
                    # Format the prompt for the instruct model
                    if not generated_text:
                        prompt = f"[Instruction]\n{instruction}\n[End of Instruction]\n"
                    else:
                        prompt = f"[Instruction]\nContinue writing the blog post section based on the following text:\n\n{generated_text[-200:]}\n[End of Instruction]\n"

                    # Make the API call to generate text
                    response = self.client.text_generation(
                        prompt=prompt,
                        model=self.model_id,
                        max_new_tokens=min(512, remaining_words * 2),
                        temperature=0.8,
                        top_p=0.95,
                        do_sample=True
                    )
                    new_text = response.strip()

                    # Filter out repeated sentences
                    sentences = new_text.split(". ")
                    filtered_sentences = []
                    for sentence in sentences:
                        if sentence not in seen_phrases:
                            filtered_sentences.append(sentence)
                            seen_phrases.add(sentence)
                    new_text = ". ".join(filtered_sentences).strip()

                    # Append new text if it's substantial
                    if new_text and len(new_text.split()) > 20:
                        generated_text += " " + new_text
                        generated_text = self.deduplicate_text(generated_text, max_repeats=1)

                    logging.info(f"Generated {len(generated_text.split())} words so far")
                    time.sleep(1)  # Respect API rate limits
                    break  # Exit retry loop on success

                except Exception as e:
                    if attempt < max_retries - 1:
                        logging.error(f"Attempt {attempt + 1} failed: {str(e)}. Retrying in 5 seconds...")
                        time.sleep(5)
                    else:
                        logging.error(f"Failed after {max_retries} attempts: {str(e)}. Skipping this chunk.")
                        break

        # Trim to the exact target word count
        return " ".join(generated_text.split()[:target_words])

    def write_content(self, outline, research_data):
        """Generate a full blog post with multiple sections."""
        sections = [
            ("# Remote Work Policies in 2025: Trends, Strategies, and Insights",
             "Write a 400-word introduction for an SEO-optimized blog post titled 'Remote Work Policies in 2025: Trends, Strategies, and Insights'. Include that 80% of U.S. employees click personal email/social media for work, 80% are in retail/service sectors with minimal HR contact. Highlight remote work trends for 2025, hybrid policies, and employee retention benefits.", 400),
            ("## Current Trends in Remote Work Policies for 2025",
             "Write a 600-word section on current trends in remote work policies for 2025. Focus on hybrid policies, employee retention strategies, and emerging tools for remote work, based on HR trends.", 600),
            ("## Implementation Strategies for Remote Work Policies in 2025",
             "Write a 600-word section on strategies to implement remote work policies in 2025. Include best practices for hybrid work, tools for productivity, and retaining employees remotely.", 600),
            ("## Benefits and Challenges of Remote Work Policies in 2025",
             "Write a 600-word section on benefits (e.g., employee retention, flexibility) and challenges (e.g., isolation, tech issues) of remote work policies in 2025.", 600),
            ("## Conclusion: Shaping Remote Work Policies for 2025 Success",
             "Write a 200-word conclusion for an SEO blog post. Summarize remote work trends, strategies, and benefits for 2025, emphasizing hybrid policies and employee retention. End with a call-to-action encouraging HR leaders to adopt these policies.", 200)
        ]

        # Initialize the blog post with front matter
        full_content = (
            "---\n"
            "title: \"Remote Work Policies in 2025: Trends, Strategies, and Insights\"\n"
            "keywords: remote work, hybrid policies, employee retention\n"
            "description: \"Discover trends, strategies, and insights for remote work policies in 2025, boosting employee retention and hybrid success.\"\n"
            "date: \"2025-03-23\"\n"
            "---\n"
        )

        # Generate each section
        for title, instruction, target_words in sections:
            try:
                final_text = self.generate_section(instruction, target_words)
                full_content += f"{title}\n\n{final_text}\n\n"
                logging.info(f"Completed {len(final_text.split())} words for section: {title}")
            except Exception as e:
                logging.error(f"Failed to generate {title}: {str(e)}")
                full_content += f"{title}\n\n[Error generating content: {str(e)}]\n\n"

        return full_content

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    agent = ContentAgent()
    content = agent.write_content(outline=None, research_data=None)
    print(content)