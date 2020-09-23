import os
import shutil

file_dir = os.path.dirname(os.path.abspath(__file__))
template_path = os.path.join(file_dir, 'templates')

cookiecutter_path = os.path.join(os.path.expanduser('~'), '.cookiecutters')

template_list = os.listdir(template_path)

for template_name in template_list:
    destination = os.path.join(cookiecutter_path, template_name)
    source = os.path.join(template_path, template_name);

    if(os.path.isfile(destination) or os.path.isdir(destination)):
        shutil.rmtree(destination)

    print('Copying template: ' + template_name)
    shutil.copytree(source, destination)
