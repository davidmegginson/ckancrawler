#!/usr/bin/python

from setuptools import setup

setup(name='hdxcrawler',
      version='0.1',
      description='Simple framework for crawling datasets on the Humanitarian Data Exchange',
      author='David Megginson',
      author_email='contact@megginson.com',
      url='https://github.com/davidmegginson/hdxcrawler',
      install_requires=['ckanapi'],
      packages=['hdxcrawler'],
      test_suite='tests',
)
