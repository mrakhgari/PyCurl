import requests


class Request:
    def __init__(self, url, method='GET'):
        '''
            Args:
                :param url: Base URL for the request. (e.g. http://www.example.com)
                :param method: method for the request: ``GET``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
        '''
        self.url = url
        self.method = method

    def make_request(self):
        print(self.method)
        print(self.url)
        return requests.request(self.method, self.url)
