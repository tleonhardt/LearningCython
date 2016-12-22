# wrapper.pyx
cimport alphawrap
cimport betawrap

def calc(double x):
    return (alphawrap.a(x)
            + betawrap.b(x))
