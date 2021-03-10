import requests


class Request:
    def __init__(self, url, method='GET', headers=None, queries=None, data=None, json=None):
        '''
            Args:
                :param url: Base URL for the request. (e.g. http://www.example.com)
                :param method: method for the request: ``GET``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
                :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
        '''
        self.url = url
        self.method = method
        self.headers = headers
        self.queries = queries
        self.data = data
        self.json = json

    def make_request(self):
        return requests.request(self.method, self.url, headers=self.headers, params=self.queries, data=self.data, json=self.json)
