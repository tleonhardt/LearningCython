#!/usr/bin/env bash

# Default output file name
OUT_FILE=prof

# Allow a command-line argument to override the output file name
if [ $# -gt 0 ]
    then
        OUT_FILE=$1
fi

# Run Python's built-in function-level profiler, cProfile
echo "Running Python's build-in function-level profiler, cProfile, on main.py."
echo "Output will be in file ${OUT_FILE}"
python -m cProfile -o "${OUT_FILE}" main.py
