from setuptools import setup, Extension
from Cython.Build import cythonize
setup(
    name="MyPackage",
    ext_modules=cythonize([
        'pkg/wrapper.pyx',
        'pkg/cymod/utils.pyx'
    ]),
)

    # ext_modules=cythonize([ext1, 'pkgdemo/cymod/utils.pyx']),
    # ext_modules=cythonize(['pkgdemo/wrapper.pyx', 'pkgdemo/cymod/utils.pyx']),
    # ext_modules=cythonize('pkgdemo/wrapper.pyx', include_path=[
    #     'pkgdemo/wrap1', 'pkgdemo/wrap2'
    #     ]),
    # package_dir={'pkgdemo':'pkgdemo', 'pkgdemo/cymod':'pkgdemo/cymod'},
    # packages=find_packages('pkgdemo'),

