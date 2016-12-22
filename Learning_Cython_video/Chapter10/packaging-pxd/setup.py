# setup.py
from setuptools import setup
from Cython.Build import cythonize

setup(
    name='AnimalSounds',
    version='0.1',
    ext_modules=cythonize([
        'tools/kittens.pyx',
        'tools/utils/puppies.pyx',
    ])
)
