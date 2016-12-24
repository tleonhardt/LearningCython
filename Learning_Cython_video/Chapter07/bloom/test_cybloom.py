# Import our Cython module
import cybloom

def test_not_in():
    bf = cybloom.Bloom(10000, 0.01)
    assert(False == (b'hello' in bf))

def test_in():
    bf = cybloom.Bloom(10000, 0.01)
    bf.add(b'hello')
    assert(False == (b'hello' in bf))
