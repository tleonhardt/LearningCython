cdef extern from "hello.h":
    char* f()

cpdef callf():
    return f()
