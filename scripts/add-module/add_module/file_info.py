from PyInquirer import prompt

def get_file_info():
    return prompt([
        {
            "type": "input",
            "name": "file_path",
            "message": "Path for new file",
            "default": "./"
        },
        {
            "type": "input",
            "name": "file_name",
            "message": "File name (don't include .py)"
        }
    ])
