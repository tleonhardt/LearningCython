#!/usr/bin/env bash

# Need to pass the -b option to indicate that we want to build
# The -a option generates an HTML annotation file with a line-by-line indication of which code is
#     native and which code interacts with the Python interpreter.
cythonize -b -a taxcode.pyx
