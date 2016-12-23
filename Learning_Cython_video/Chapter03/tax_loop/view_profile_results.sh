#!/usr/bin/env bash

# Default profile file name
PROF_FILE=prof

# Allow a command-line argument to override the profile file name
if [ $# -gt 0 ]
    then
        PROF_FILE=$1
fi

# Run Python's built-in profile statistics browser, pstats, on profile file
echo "Running Python's built-in profile statistics browser, pstats, on profile file '${PROF_FILE}'"
echo "Type 'help' to get a list of commands."
echo "The command you will use most frequently is 'stats', but by default it produces too much data."
echo "The first thing you need to do is move the paths names.  To do this enter command 'strip'"
echo "Run 'stats' again and things look better, but there is still too much data."
echo "To limit the display to 10 items, run 'stats 10'"
echo "This output is much more manageable.  But to get meaningful data, you need to sort the results."
echo "Type 'sort' to see sorting options."
echo "The most useful one is to sort by the total time cost."
echo "Type 'sort tottime'.  Then type 'stats 10' again."
echo ""
echo "tl;dr - Enter the following sequence of commands:"
echo "strip"
echo "sort tottime"
echo "stats 10"
echo "quit"
echo ""
python -m pstats "${PROF_FILE}"
