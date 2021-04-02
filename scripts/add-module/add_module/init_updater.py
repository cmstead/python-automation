import os

def update_init(file_info):
    full_path = os.path.realpath(os.path.join(
        file_info["file_path"], "__init__.py"))

    with open(full_path, "a") as file_writer:
        file_writer.write(f"from .{file_info['file_name']} import *")