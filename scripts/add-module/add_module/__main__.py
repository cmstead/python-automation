#!/usr/bin/env python3.8

import os
import sys

from .file_info import get_file_info
from .file_writer import write_file
from .init_updater import update_init

run_command = os.system

def main():
    file_info = get_file_info()

    write_file(file_info)
    update_init(file_info)

    

if __name__ == "__main__":
    main()
