#!/usr/bin/env bash

# Default profile file name
PROF_FILE=prof

# Allow a command-line argument to override the profile file name
if [ $# -gt 0 ]
    then
        PROF_FILE=$1
fi

# Run 3rd-party snakeviz GUI tool for viewing profile file
# NOTE: Requires installation with "pip install -U --pre snakeviz"
echo "Running 3rd-party 'snakeviz' browser-based graphical viewr for output of Python's cProfile on file '${PROF_FILE}'"
snakeviz "${PROF_FILE}"
