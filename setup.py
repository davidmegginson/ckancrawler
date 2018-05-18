#!/usr/bin/python

from setuptools import setup

setup(name='ckancrawler',
      version='0.1',
      description='Simple framework for iterating through CKAN datasets',
      author='David Megginson',
      author_email='contact@megginson.com',
      url='https://github.com/davidmegginson/ckancrawler',
      install_requires=['ckanapi'],
      packages=['ckancrawler'],
      test_suite='tests',
)
