"""..."""
from textnode import TextNode
from copy_folder_structure import (
    prepare_folder_structure,
    copy_folder_structure
)

SOURCE_PATH = "./static"
DEST_PATH = "./public"


def main():
    """..."""
    text_node = TextNode("This is a text node", "bold", "https://www.google.com")
    print(text_node)
    prepare_folder_structure(DEST_PATH)
    copy_folder_structure(SOURCE_PATH, DEST_PATH)


if __name__ == "__main__":
    main()
