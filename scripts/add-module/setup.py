import pathlib
from setuptools import setup, find_packages

CURRENT_DIR = pathlib.Path(__file__).parent
README_CONTENT = (CURRENT_DIR / "README.md").read_text()

setup(
    name='add-module',
    version='0.1.0',
    packages=["add_module"],
    author="Chris Stead",
    author_email="cmstead@gmail.com",
    url="https://github.com/cmstead/add-module#readme",
    platforms=['any'],
    description="Add module to existing directory",
    license='MIT',
    long_description=README_CONTENT,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3"
    ],
    entry_points={
        "console_scripts": [
            "add-module = add_module.__main__:main"
        ]
    }
)