import unittest
import ckaniterator

class TestCKANIterator(unittest.TestCase):
    """Test the ckaniterator.CKANIterator class"""

    def setUp(self):
        # no delay, since we'll look at only a small number of packages
        self.iterator = ckaniterator.CKANIterator(delay=0)

    def test_all(self):
        """Basic access"""
        self.assertValidResults()

    def test_tag_query(self):
        """Search for a specific tag"""
        self.assertValidResults('tags:demo')

    def test_text_query(self):
        """Search for a text match"""
        self.assertValidResults('demo')

    def assertValidResults(self, query=None, sort=None):
        """Check that we have valid results for a query"""
        max_packages = 5 # enough to test
        seen_package = False
        for i, package in enumerate(self.iterator.packages()):
            seen_package = True
            self.assertTrue(package['name'] is not None)
            self.assertTrue(len(package['resources']) > 0)
            if i >= max_packages:
                break # don't need to see too many packages
        self.assertTrue(seen_package)
