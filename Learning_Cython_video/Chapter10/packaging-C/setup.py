from setuptools import setup, Extension
from Cython.Build import cythonize

ext = Extension('wrapper',
        sources=[
            'pkgdemo/wrapper.pyx',
            # 'pkgdemo/wrap1/alpha.c',
            # 'pkgdemo/wrap2/beta.c',
            ])

setup(
    name="MyWrapper",
    version="0.1",
    ext_modules=cythonize([ext]),
    )
