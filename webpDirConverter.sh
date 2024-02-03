#!/usr/bin/bash

# Converts all png files in a directory to webp

# Usage:
#   - move this script into desired directory
#   - run `./webpDirConverter.sh`

for FILE in ./*.png; do
  fileName=$(basename $FILE .png)
  convert $fileName.png $fileName.webp
  echo "$FILE converted to webp"
done
