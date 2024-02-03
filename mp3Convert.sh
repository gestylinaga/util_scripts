#!/usr/bin/bash

# Converts .wav audio file to .mp3 file (with matching filename)

# Usage:
# - run `./mp3Convert.sh filename`

name=$1
ffmpeg -i $name.wav -vn -ar 44100 -ac 2 -b:a 192k $name.mp3
