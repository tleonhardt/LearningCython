# cython: language_level=3
cimport cbloom

cdef class Bloom:
    cdef cbloom.bloom b
    cdef cbloom.bloom* pb
    def __cinit__(self, int entries, double error):
        self.pb = &self.b
        result = cbloom.bloom_init(
                self.pb, entries, error)
        print('init result: ', result)
        if result==1:
            raise Exception('bloom_init failed.')
    def __dealloc__(self):
        cbloom.bloom_free(self.pb)

    def add(self, bytes item):
        cdef int result = cbloom.bloom_add(
                self.pb,
                <void*>item, len(item))
        if result == 1:
            raise Exception('This item has already been added.')

    def __contains__(self, bytes item):
        cdef int result = cbloom.bloom_check(
                self.pb,
                <void*>item, len(item))
        return result == 1





