import shutil

def delete_template(path):
    shutil.rmtree(path)

def copy_template(source_path, destination_path):
    shutil.copytree(source_path, destination_path)