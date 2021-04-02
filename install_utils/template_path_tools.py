import os


def get_template_directory():
    file_dir = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(file_dir, "..", "templates")


def get_template_list():
    template_path = get_template_directory()

    return os.listdir(template_path)


def get_cookiecutter_path():
    return os.path.join(os.path.expanduser('~'), '.cookiecutters')


def get_template_destination(template_name):
    cookiecutter_path = get_cookiecutter_path()

    return os.path.join(cookiecutter_path, template_name)


def get_template_source(template_name):
    template_path = get_template_directory()

    return os.path.join(template_path, template_name)


def destination_path_exists(destination_path):
    return os.path.isfile(destination_path) or os.path.isdir(destination_path)

def get_template_name():
    return os.sys.argv[1]
