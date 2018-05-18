"""Simple command-line demo"""

from . import Crawler

crawler = Crawler()

print("Demo: all packages from demo.ckan.org matching 'demo'")
for package in crawler.packages(q='demo'):
    print("  " + package['name'])
