import os


def write_file(file_info):
    full_path = os.path.realpath(os.path.join(
        file_info["file_path"], f"{file_info['file_name']}.py"))

    with open(full_path, "w") as file_writer:
        file_writer.write("if __name__ == \"__main__\":\n    pass")
