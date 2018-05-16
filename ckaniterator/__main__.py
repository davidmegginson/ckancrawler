"""Simple command-line demo"""

from . import CKANIterator

iterator = CKANIterator()

print("Demo: all packages from demo.ckan.org matching 'demo'")
for package in iterator.packages(q='demo'):
    print("  " + package['name'])
