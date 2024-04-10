#!/bin/bash

FILE_PATH="file.txt"

grep '^\([0-9]\{3\}-\|([0-9]\{3\}) \)[0-9]\{3\}-[0-9]\{4\}$' $FILE_PATH
