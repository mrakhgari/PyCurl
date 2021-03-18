import requests
from exceptions import TimeOut


class Request:
    def __init__(self, url, method='GET', headers=None, queries=None, 
            data=None, json=None, file=None, timeout=None):
        """Constructs a :class:`Request <Request>`.

        :param url: URL for the new :class:`Request` object.
        :param method: method for the new :class:`Request` object: ``GET``, ``POST``, ``PUT``, ``PATCH``, or ``DELETE``.
        :param headers: (optional) Dictionary of HTTP Headers to send with the :class:`Request`.
        :param queries: (optional) Dictionary, list of tuples or bytes to send
            in the query string for the :class:`Request`.
        :param data: (optional) Dictionary, list of tuples, bytes, or file-like
            object to send in the body of the :class:`Request`.
        :param json: (optional) A JSON serializable Python object to send in the body of the :class:`Request`.
        :param file: (optional) Dictionary of ``'name': file-like-objects`` (or ``{'name': file-tuple}``) for multipart encoding upload.
            ``file-tuple`` can be a 2-tuple ``('filename', fileobj)``, 3-tuple ``('filename', fileobj, 'content_type')``
            or a 4-tuple ``('filename', fileobj, 'content_type', custom_headers)``, where ``'content-type'`` is a string
            defining the content type of the given file and ``custom_headers`` a dict-like object containing additional headers
            to add for the file.
        :param timeout: (optional) How many seconds to wait for the server to send data
            before giving up, as a float, or a :ref:`(connect timeout, read
            timeout) <timeouts>` tuple.
        :type timeout: float or tuple
        """

        self.url = url
        self.method = method
        self.headers = headers
        self.queries = queries
        self.data = data
        self.json = json
        self.file = file
        self.timeout = timeout

    def make_request(self):
        try:
            return requests.request(self.method, self.url, headers=self.headers, 
                params=self.queries, data=self.data, json=self.json, files=self.file, timeout=self.timeout)
        except requests.exceptions.Timeout:
            raise TimeOut(self.timeout)
