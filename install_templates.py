import os

from install_template import install_template
from install_utils.template_path_tools import get_template_list

def install_templates():
    template_list = get_template_list()

    for template_name in template_list:
        install_template(template_name)

if __name__ == "__main__":
    install_templates()