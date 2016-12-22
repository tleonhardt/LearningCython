cdef extern from "shoco.h":

    #size_t shoco_compress(const char * const shoco_restrict in, size_t len, char * const shoco_restrict out, size_t bufsize);
    #size_t shoco_decompress(const char * const shoco_restrict in, size_t len, char * const shoco_restrict out, size_t bufsize);
    long shoco_compress(const char * inp, long len, char * out, long bufsize);
    long shoco_decompress(const char * inp, long len, char * out, long bufsize);



