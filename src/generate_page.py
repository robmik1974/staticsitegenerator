"""Generate HTML from a markdown file"""
import re
from block_to_html import markdown_to_html_node


def extract_title(markdown):
    """Returns header from the markdown"""
    for line in markdown.split("\n"):
        if re.match(r'^# .*', line):
            return line
    raise ValueError("There is no header in the markdown")


def generate_page(from_path, template_path, dest_path):
    """Generetes final html page"""
    print("Generating page from {from_path} to {dest_path} using {template_path}")
    fobj = open(from_path, "r", encoding='utf8')
    markdown = fobj.read()
    fobj.close()

    fobj = open(template_path, "r", encoding='utf8')
    template = fobj.read()
    fobj.close()

    node = markdown_to_html_node(markdown)
    html = node.to_html()

    title = extract_title(markdown)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    fobj = open(dest_path, "w", encoding="utf-8")
    fobj.write(template)
    fobj.close()
