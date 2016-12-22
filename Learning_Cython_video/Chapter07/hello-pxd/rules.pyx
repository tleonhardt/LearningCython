# cython: language_level=3
# cython: boundscheck=False
# cython: wraparound=False

ctypedef unsigned char byte


cpdef byte flat(byte r, byte g,
        byte b):
    return (r + g + b) // 3


cpdef colorimetric(byte r,
        byte g, byte b):
    """
    wikipedia.org/wiki/Grayscale
    """
    return <byte>(
            0.2126 * r +
            0.7152 * g +
            0.0722 * b
           ) // 3


