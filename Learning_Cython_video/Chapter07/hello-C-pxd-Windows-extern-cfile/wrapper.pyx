cdef extern from "hello.c":
    char* f()

cpdef callf():
    return f()
