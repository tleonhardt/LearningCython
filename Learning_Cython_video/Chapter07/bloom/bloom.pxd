cdef extern from "bloom.h":
    struct bloom:
        pass
    int bloom_init(bloom * bloom, int entries, double error)
    int bloom_check(bloom * bloom, const void * buffer, int len)
    int bloom_add(bloom * bloom, const void * buffer, int len)
    void bloom_free(bloom * bloom)
