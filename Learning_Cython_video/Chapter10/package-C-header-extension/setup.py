from setuptools import setup, Extension
from Cython.Build import cythonize
ext1 = Extension('pkg.wrapper',
        sources=[
            'pkg/wrapper.pyx',
            'pkg/extlib/external.c',
            ])
ext2 = Extension('pkg.cymod.utils',
        sources=['pkg/cymod/utils.pyx'])
setup(
    name="MyPackage",
    version="0.1",
    ext_modules=cythonize([ext1, ext2]),
)

    # ext_modules=cythonize([ext1, 'pkgdemo/cymod/utils.pyx']),
    # ext_modules=cythonize(['pkgdemo/wrapper.pyx', 'pkgdemo/cymod/utils.pyx']),
    # ext_modules=cythonize('pkgdemo/wrapper.pyx', include_path=[
    #     'pkgdemo/wrap1', 'pkgdemo/wrap2'
    #     ]),
    # package_dir={'pkgdemo':'pkgdemo', 'pkgdemo/cymod':'pkgdemo/cymod'},
    # packages=find_packages('pkgdemo'),
