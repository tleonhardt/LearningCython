# distutils: libraries = hello
# distutils: library_dirs = .
# distutils: include_dirs = .

cdef extern from "hello.h":
    char* f()

cpdef callf():
    return f()
