"""..."""
import re

BLOCK_TYPE_PARAGRAPH = "paragraph"
BLOCK_TYPE_HEADING = "heading"
BLOCK_TYPE_CODE = "code"
BLOCK_TYPE_QUOTE = "quote"
BLOCK_TYPE_UNORDERED_LIST = "unordered_list"
BLOCK_TYPE_ORDERED_LIST = "ordered_list"


def markdown_to_blocks(markdown):
    """Splits document into sections"""
    markdown = markdown.strip()
    list_of_blocks = re.split(r'\n\s*\n', markdown)
    return list_of_blocks


def block_to_block_type(block_of_markdown):
    """Checks type of blok in markdow"""
    lines = block_of_markdown.split("\n")
    if block_of_markdown.startswith("#"):
        if re.match(r"#{1,6}\ .*", block_of_markdown):
            return BLOCK_TYPE_HEADING
    if block_of_markdown.startswith("`"):
        if re.match(r"^`{3}\n.*\n`{3}$", block_of_markdown, re.MULTILINE):
            return BLOCK_TYPE_CODE
    if block_of_markdown.startswith(">"):
        for line in lines:
            if not re.match(r"^>", line):
                return BLOCK_TYPE_PARAGRAPH
            return BLOCK_TYPE_QUOTE
    if block_of_markdown.startswith("*") or block_of_markdown.startswith("-"):
        for line in lines:
            if not re.match(r"^\*|-", line):
                return BLOCK_TYPE_PARAGRAPH
        return BLOCK_TYPE_UNORDERED_LIST
    if block_of_markdown.startswith("1. "):
        number = 1
        for line in lines:
            if not re.match(re.escape(str(number)) + r"\.\ ", line):
                return BLOCK_TYPE_PARAGRAPH
            number += 1
        return BLOCK_TYPE_ORDERED_LIST
    return BLOCK_TYPE_PARAGRAPH
