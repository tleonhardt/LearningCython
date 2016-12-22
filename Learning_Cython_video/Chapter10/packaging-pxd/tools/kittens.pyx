# kittens.pyx
from .utils cimport puppies

cpdef sound():
    print("Kittens don't: ")
    print(puppies.sound())
    print
    return 'Meow!'
