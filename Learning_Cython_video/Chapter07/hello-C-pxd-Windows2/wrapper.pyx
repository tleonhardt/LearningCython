# distutils: libraries = hello

cdef extern from "hello.h":
    char* f()

cpdef callf():
    return f()

# distutils: library_dirs = .
# distutils: include_dirs = .
