#!/usr/bin/bash

# Converts all image files in a directory to webp (default is png files)

# USAGE:
#   - move this script into desired directory
#   - run `./webpDirConverter.sh`
#
# OPTIONAL: 
#   - pass file extension as an argument
#   - example: `./webpDirConverter.sh jpg` to convert all `.jpg`'s in a directory

ext=$1

if [[ $ext == "" ]]; then
  ext="png"
fi

for FILE in ./*.$ext; do
  fileName=$(basename $FILE .$ext)
  convert $fileName.$ext $fileName.webp
  echo "$FILE converted to webp"
done
