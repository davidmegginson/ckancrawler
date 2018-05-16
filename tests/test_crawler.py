import unittest
import hdxcrawler

class StopTestException(Exception):
    pass

class TestCrawler(unittest.TestCase):
    """Test the hdxcrawler.Crawler class"""

    def setUp(self):
        self.crawler = hdxcrawler.Crawler()

    def test_access(self):
        """Basic access"""
        self.crawler.crawl('tags:xxxyyyzzz') #unlikely tag

    def test_package(self):
        """Processing packages"""

        seen_package = False

        def callback(package):
            nonlocal seen_package
            seen_package = True
            self.assertTrue(package['name'] is not None)
            print(package)
            raise StopTestException # we don't need to see every package
        
        self.crawler.package_callback = callback

        with self.assertRaises(StopTestException):
            self.crawler.crawl('tags:hxl')

        self.assertTrue(seen_package)

    def test_resource_callback(self):
        """Processing resources"""

        seen_resource = False

        def callback(package, resource):
            nonlocal seen_resource
            seen_resource = True
            self.assertTrue(package['name'] is not None)
            self.assertTrue(resource['name'] is not None)
            raise StopTestException # we don't need to see every resource
        
        self.crawler.resource_callback = callback

        with self.assertRaises(StopTestException):
            self.crawler.crawl('tags:hxl')

        self.assertTrue(seen_resource)

    
