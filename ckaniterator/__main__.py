"""Simple command-line demo"""

from . import CKANIterator

iterator = CKANIterator()

print("Demo: all packages from demo.ckan.org tagged \"demo\"")
for package in iterator.packages('tags:demo'):
    print("  " + package['name'])
