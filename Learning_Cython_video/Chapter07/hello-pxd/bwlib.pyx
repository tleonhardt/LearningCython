# cython: language_level=3
# cython: boundscheck=False
# cython: wraparound=False

from rules import (
        flat, colorimetric
        )


ctypedef unsigned char byte


def makegrey(byte[:,:,:] data):
    cdef int i, j, N, M
    N, M = data.shape[:2]
    cdef byte r, g, b, x

    for i in range(N):
        for j in range(M):
            r, g, b = data[i, j]
            x = flat(r, g, b)
            data[i, j] = x



