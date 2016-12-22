# distutils: libraries = "bloom"
# distutils: library_dirs = "."
cimport bloom

cdef class Bloom:
    cdef bloom.bloom b
    cdef bloom.bloom * pb
    def __cinit__(self, n, error):
        self.pb = &self.b
        result = bloom.bloom_init(self.pb, n, error)
        if result == 1:
            raise Exception('bloom_init failed.')

    def __dealloc__(self):
        bloom.bloom_free(self.pb)

    def add(self, bytes item):
        result = bloom.bloom_add(self.pb, <void*>item, len(item))
        if result == 1:
            raise Exception('This item has already been added!')

    def __contains__(self, bytes item):
        result = bloom.bloom_check(self.pb, <void*>item, len(item))
        return result==1
