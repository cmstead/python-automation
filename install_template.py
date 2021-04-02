from install_utils.template_filesystem_tools import \
    delete_template, \
    copy_template

from install_utils.template_path_tools import \
    get_template_destination, \
    get_template_source, \
    destination_path_exists, \
    get_template_name


def install_template(template_name):
    destination = get_template_destination(template_name)
    source = get_template_source(template_name)

    if(destination_path_exists(destination)):
        delete_template(destination)

    print('Copying template: ' + template_name)

    copy_template(source, destination)


if __name__ == "__main__":
    template_name = get_template_name()

    install_template(template_name)
