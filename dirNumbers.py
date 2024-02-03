#!/usr/bin/env python3

# Renames all files in a directory (with a 3 character extension ie: png/jpg/mp4)
# to an incremental number with the original file extension

# USAGE:
#   - copy this file into desired directory
#   - change `i` variable to desired starting number
#   - run `./renameToNumbers.py`

import os

thisFile = "dirNumbers.py" # saved to variable to ignore in rename
i = 1 # starting number

for file in os.listdir("./"):
    # only work on regular files (exclude directories)
    if not os.path.isfile(file):
        continue

    # ignore this .py file
    if file != thisFile:
        fileName = file[:-4]
        ext = file[-4:]
        print(f"{file} => {i}{ext}")
        os.rename(file, f"{i}{ext}")
        i += 1
