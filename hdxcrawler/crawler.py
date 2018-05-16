import ckanapi, time

class Crawler:

    DEFAULT_CKAN_URL='https://data.humdata.org'
    """Base URL for the CKAN instance"""

    DELAY = 1
    """Time delay in seconds between datasets, to give HDX a break."""

    CHUNK_SIZE=100
    """Number of dataset records to read at once"""

    def __init__(self, package_callback=None, resource_callback=None, ckan_url=None, apikey=None, user_agent=None):
        """Set up the crawler.
        Callbacks:
            package_callback(package)
            resource_callback(package, resource)
        @param package_callback: function to call for each package found (default: None)
        @param resource_callback: function to call for each resource found (default: None)
        @param ckan_url: the CKAN URL to use (default: https://data.humdata.org)
        @param apikey: the CKAN API key to use for non-anonymous access (default: None)
        @param user_agent: the HTTP user-agent string to send for special cases (default: None)
        """
        
        self.package_callback = package_callback
        """Function to call for each matching package"""

        self.resource_callback = resource_callback
        """Function to call for each resource in each matching package"""
        
        if ckan_url is None:
            ckan_url = Crawler.DEFAULT_CKAN_URL

        self.ckan = ckanapi.RemoteCKAN(ckan_url, apikey=apikey, user_agent=user_agent)
        """CKAN instance that we're using"""

    def crawl(self, query):
        """Execute a query against HDX, and trigger callbacks for each matching package.
        Uses \L{package_callback} and \L{resource_callback} if assigned
        Pauses for DELAY between each operation.
        @param query: a CKAN search query (e.g. "tags:hxl")
        """
        start = 0
        result_count = 99999 # just a big number
        while start < result_count:
            result = self.ckan.action.package_search(fq=query, start=start, rows=Crawler.CHUNK_SIZE)
            result_count = result['count']
            for package in result['results']:
                if self.package_callback is not None:
                    self.package_callback(package)
                    time.sleep(Crawler.DELAY)
                if self.resource_callback is not None:
                    for resource in package['resources']:
                        self.resource_callback(package, resource)
                        time.sleep(Crawler.DELAY)
            time.sleep(Crawler.DELAY)

    def touch(self, package):
        """Convenience method to update only a package's date.
        @param package: the package object to update.
        """
        pass
