"""..."""
import re


def markdown_to_blocks(markdown):
    """Splits document into sections"""
    markdown = markdown.strip()
    list_of_blocks = re.split(r'\n\s*\n', markdown)
    return list_of_blocks
