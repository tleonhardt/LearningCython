# puppies.pyx
from .. cimport kittens

cpdef sound():
    print("Puppies don't: ")
    print(kittens.sound())
    print()
    return 'Bark!'
