"""Simple command-line demo"""

from . import Crawler

def package_callback(package):
    print("    " + package['name'])

def resource_callback(package, resource):
    print("        " + resource['name'])

crawler = Crawler(package_callback=package_callback, resource_callback=resource_callback)

print("Demo: all packages tagged \"hxl\"")
crawler.crawl('tags:hxl')
