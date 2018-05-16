import ckanapi, time

class CKANIterator:

    CHUNK_SIZE=100
    """Number of dataset records to read at once"""

    def __init__(self, ckan_url='https://demo.ckan.org', apikey=None, user_agent=None, delay=1):
        """Set up the iterator.
        @param ckan_url: the CKAN URL to use (default: https://data.humdata.org)
        @param apikey: the CKAN API key to use for non-anonymous access (default: None)
        @param user_agent: the HTTP user-agent string to send for special cases (default: None)
        @param delay: the delay, in seconds, after returning each result (default: 1)
        """
        self.ckan = ckanapi.RemoteCKAN(ckan_url, apikey=apikey, user_agent=user_agent)
        """CKAN instance that we're using"""

        self.delay = delay
        """Delay in seconds after each result (to give the server a break)"""

    def packages(self, q=None, fq=None, sort=None):
        """Execute a query against HDX, and yield a result for each matching package.
        Pauses for \L{delay} after each operation.
        @param q: a CKAN search query (e.g. "population")
        @param fq: a CKAN filter query (e.g. "tags:hxl")
        @param sort: a CKAN sort specification (e.g. "relevance asc, metadata_modified desc")
        """
        start = 0
        while True:
            result = self.ckan.action.package_search(q=q, fq=fq, sort=sort, start=start, rows=CKANIterator.CHUNK_SIZE)
            result_count = len(result['results'])
            if result_count <= 0:
                break
            # iterate through the results
            for package in result['results']:
                yield package
                time.sleep(self.delay)
            start += result_count

    def update_package(self, package):
        self.ckan.call_action('package_update', package)
