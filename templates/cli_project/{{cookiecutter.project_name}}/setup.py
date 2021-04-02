import pathlib
from setuptools import setup, find_packages

CURRENT_DIR = pathlib.Path(__file__).parent
README_CONTENT = (CURRENT_DIR / "README.md").read_text()

setup(
    name='{{cookiecutter.project_name}}',
    version='0.1.0',
    packages=["{{cookiecutter.source_directory}}"],
    author="{{cookiecutter.author}}",
    author_email="{{cookiecutter.email}}",
    url="https://github.com/{{cookiecutter.github_username}}/{{cookiecutter.project_name}}#readme",
    platforms=['any'],
    description="{{cookiecutter.description}}",
    license='{{cookiecutter.license}}',
    long_description=README_CONTENT,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: {{cookiecutter.python_version}}"
    ],
    entry_points={
        "console_scripts": [
            "{{cookiecutter.project_name}} = {{cookiecutter.source_directory}}.__main__:main"
        ]
    }
)