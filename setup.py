#!/usr/bin/python

from setuptools import setup

setup(name='ckaniterator',
      version='0.1',
      description='Simple framework for iterating through CKAN datasets',
      author='David Megginson',
      author_email='contact@megginson.com',
      url='https://github.com/davidmegginson/ckaniterator',
      install_requires=['ckanapi'],
      packages=['ckaniterator'],
      test_suite='tests',
)
