#!/usr/bin/env python3.8

import os
import sys

run_command = os.system

def main():
    args = sys.argv[1:]
    run_command(f"echo hello")

if __name__ == "__main__":
    main()
