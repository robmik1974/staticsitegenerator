"""..."""
import os
import shutil
import pathlib
import time


def prepare_folder_structure(dest_folder):
    """Prepare empty destination folders' structure"""
    if os.path.exists(dest_folder):
        shutil.rmtree(dest_folder)
    os.mkdir(dest_folder)
    time.sleep(10)


def copy_folder_structure(source_path, dest_path):
    """Copy source folders' structure into destination keeping folders' structure"""
    paths = os.listdir(source_path)
    for item in paths:
        source = os.path.join(source_path, item)
        dest = os.path.join(dest_path, item)
        if os.path.isfile(source):
            if not os.path.exists(dest_path):
                os.mkdir(dest_path)
            shutil.copy(pathlib.Path(source), pathlib.Path(dest))
        else:
            copy_folder_structure(source, dest)
