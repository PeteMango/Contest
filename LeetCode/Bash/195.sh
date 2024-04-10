#!/bin/bash

FILE_PATH="file.txt"

if [ -f "$FILE_PATH" ]; then
    counter=1

    while IFS= read -r line; do
        if [ $counter == 10 ]; then
            echo $line
        fi

        ((counter++))
    done < "$FILE_PATH"
else
    echo "Error: File does not exist."
fi
