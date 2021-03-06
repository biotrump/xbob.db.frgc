#!/usr/bin/env python
# vim: set fileencoding=utf-8 :
# author: Manuel Guenther <manuel.guenther@idiap.ch>
# date:   Wed Feb 13 12:35:29 CET 2013

from setuptools import setup, find_packages

# The only thing we do in this file is to call the setup() function with all
# parameters that define our package.
setup(

    name='xbob.db.frgc',
    version='1.2.1a0',
    description='Database Access API of the Face Recognition Grand Challenge (FRGC) ver2.0 image database for Bob',
    url='http://github.com/bioidiap/xbob.db.frgc',
    license='GPLv3',
    author='Manuel Guenther',
    author_email='manuel.guenther@idiap.ch',
    long_description=open('README.rst').read(),

    # This line is required for any distutils based packaging.
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,

    install_requires=[
      'setuptools',
      'six',  # py2/3 compatibility library
      'bob',  # base signal proc./machine learning library
      'xbob.db.verification.utils>=1.0.0' # defines a set of utilities for face verification databases like this one.
    ],

    namespace_packages = [
      'xbob',
      'xbob.db',
      ],

    entry_points = {
      # bob database declaration
      'bob.db': [
        'frgc = xbob.db.frgc.driver:Interface',
        ],

      # bob unittest declaration
      'bob.test': [
        'frgc = xbob.db.frgc.test:FRGCDatabaseTest',
        ],
      },

    classifiers = [
      'Development Status :: 4 - Beta',
      'Intended Audience :: Developers',
      'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
      'Natural Language :: English',
      'Programming Language :: Python',
      'Programming Language :: Python :: 3',
      'Topic :: Scientific/Engineering :: Artificial Intelligence',
      'Topic :: Database :: Front-Ends',
      ],
)
