#!/usr/bin/env python3

# Renames all files in a directory to an incremental number while keeping the 
# original file extension

# USAGE:
#   - copy this file into desired directory
#   - run `./dirNumbers.py`
#   - optional -- pass number for starting index (otherwise defaults to 1):
#       - run `./dirNumbers.py 42` to start filenames at `42`

import os
from sys import argv

this_file = "dirNumbers.py" # saved to variable to ignore in rename
try:
    i = int(argv[1]) # argument passed as starting number
except IndexError:
    i = 1 # defaults to `1` if no argument is passed
except ValueError:
    # Prints error on invalid argument & exits
    print("Value Error: argument passed is not a number")
    exit()

for file in os.listdir("./"):
    # only work on regular files (exclude directories)
    if not os.path.isfile(file):
        continue

    # ignore this .py file
    if file != this_file:
        # filename / extension parsing
        file_name_as_list = file.split(".")
        filename = "".join(file_name_as_list[:-1])
        ext = "".join(file_name_as_list[-1:])

        # results & rename
        print(f"{file} => {i}.{ext}")
        os.rename(file, f"{i}.{ext}")
        i += 1
