import ckancrawler, unittest

class TestCrawler(unittest.TestCase):
    """Test the ckancrawler.Crawler class"""

    def setUp(self):
        # no delay, since we'll look at only a small number of packages
        self.crawler = ckancrawler.Crawler(delay=0)

    def test_no_query(self):
        """Iterate through all packages"""
        self.assertValidResults()

    def test_search_query(self):
        """Text search query"""
        self.assertValidResults(q='demo')

    def test_filter_query(self):
        """Filter query"""
        self.assertValidResults(fq='tags:demo')

    def assertValidResults(self, q=None, fq=None, sort=None):
        """Check that we have valid results for a query"""
        max_packages = 5 # enough to test
        seen_package = False
        for i, package in enumerate(self.crawler.packages(q=q, fq=fq, sort=sort)):
            seen_package = True
            self.assertTrue(package['name'] is not None)
            if i >= max_packages:
                break # don't need to see too many packages
        self.assertTrue(seen_package)
