#!/usr/bin/env python3

# Renames all files in a directory to an incremental number while keeping the 
# original file extension

# USAGE:
#   - copy this file into desired directory
#   - change `i` variable to desired starting number
#   - run `./renameToNumbers.py`

import os

this_file = "dirNumbers.py" # saved to variable to ignore in rename
i = 1 # starting number

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
