from distutils.core import setup, Extension

module1 = Extension('func',
                    sources = ['wrapper.c','func.c'],
                    #extra_objects = ['func.o'],
                    )

module1 = Extension('read',
                    sources = ['r_wrapper.c','read.c'],
                    #extra_objects = ['func.o'],
                    )

setup(name = 'func', version = '1.0.0', ext_modules = [module1])
setup(name = 'read', version = '1.0.0', ext_modules = [module1])