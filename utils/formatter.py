# utils/formatter.py
import re

class Formatter:
    def __init__(self):
        self.max_line_length = 80  # For readability

    def format_markdown(self, content: str) -> str:
        """
        Format content into clean Markdown with proper spacing and structure.
        
        Args:
            content (str): Raw content string
        
        Returns:
            str: Formatted Markdown content
        """
        # Normalize whitespace
        content = re.sub(r'\s+', ' ', content.strip())
        
        # Ensure proper heading spacing
        content = re.sub(r'^(#+)\s*([^#].*)$', r'\1 \2\n', content, flags=re.MULTILINE)
        
        # Add line breaks after paragraphs
        content = re.sub(r'([^\n])\n([^\n#])', r'\1\n\n\2', content)
        
        # Wrap lines for readability
        formatted_lines = []
        for line in content.split('\n'):
            if len(line) > self.max_line_length and not line.startswith('#'):
                words = line.split()
                current_line = ""
                for word in words:
                    if len(current_line) + len(word) + 1 <= self.max_line_length:
                        current_line += f" {word}" if current_line else word
                    else:
                        formatted_lines.append(current_line)
                        current_line = word
                if current_line:
                    formatted_lines.append(current_line)
            else:
                formatted_lines.append(line)
        
        return '\n'.join(formatted_lines)

    def add_front_matter(self, content: str, title: str, keywords: list[str], description: str) -> str:
        """
        Add YAML front matter for SEO and metadata.
        
        Args:
            content (str): Blog content
            title (str): Blog title
            keywords (list[str]): SEO keywords
            description (str): Meta description
        
        Returns:
            str: Content with front matter
        """
        front_matter = f"""---
title: "{title}"
keywords: {', '.join(keywords)}
description: "{description}"
date: "2025-03-23"
---
"""
        return f"{front_matter}\n{content}"

# Example usage (for testing)
if __name__ == "__main__":
    sample_content = "#Test Title Very long text here that needs wrapping because it exceeds the maximum line length we set earlier."
    formatter = Formatter()
    formatted = formatter.format_markdown(sample_content)
    print(formatter.add_front_matter(formatted, "Test Title", ["test", "blog"], "A test blog post"))