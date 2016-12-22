# distutils: libraries = shoco
# disutils: library_dirs = "."
cimport shoco

cpdef bytes shoco_compress(str s):
    cdef bytes inp = s.encode('utf-8')
    cdef bytes out = b' '*len(inp)*2
    cdef char* cin = inp     # Same buffer
    cdef char* cout = out   # Same buffer
    cdef int newsize = shoco.shoco_compress(cin, len(inp), cout, len(out))
    if newsize >= len(out):
        raise Exception('buffer too small')
    return out[:newsize]  # Slice to correct size

cpdef str shoco_decompress(bytes x):
    cdef bytes out = b' '*len(x)*10
    cdef char* cin = x      # Same buffer
    cdef char* cout = out   # Same buffer
    cdef int newsize = shoco.shoco_decompress(cin, len(x), cout, len(out))
    if newsize >= len(out):
        raise Exception('buffer too small')
    return out[:newsize].decode('utf-8')
