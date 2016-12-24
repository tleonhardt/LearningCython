# Generate the C file with Cython
cython --embed adder.py

# Use your compiler to produce an executable and link against Python

# This works well if you are using the system Python on Mac OS X or Linux
# This produces an exectuable, but it requires your exact version of Python present to work
gcc `python-config --include` adder.c `python-config --lib` -o adder


# This sort of works for Anaconda Python, but there are issues

# My path for where Anaconda Python is installed
# PYPATH=/Users/siuser/anaconda
# PYVER=3.5
#
# gcc -I${PYPATH}/include/python${PYVER}m adder.c -L${PYPATH}/lib -lpython${PYVER}m -o adder
