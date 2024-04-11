"""..."""
import os
from generate_page import generate_page
from copy_folder_structure import (
    prepare_folder_structure,
    copy_folder_structure
)

SOURCE_PATH = "./static"
TEMPLATE_PATH = "./template.html"
DEST_PATH = "./public"
CONTENT_PATH = "./content"


def main():
    """..."""
    prepare_folder_structure(DEST_PATH)
    copy_folder_structure(SOURCE_PATH, DEST_PATH)
    generate_page(
        os.path.join(CONTENT_PATH, "index.md"),
        TEMPLATE_PATH,
        os.path.join(DEST_PATH, "index.html")
    )


if __name__ == "__main__":
    main()
