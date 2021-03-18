app_description = "PyCurl is a simple command-line tool for transferring data with URL developed using Python."

url_help = "The URL syntax is protocol-dependent. You'll find a detailed description in RFC 3986."
method_help = "The method that you use for sending data."
header_help = '(HTTP) Extra header to include in the request when sending HTTP to a server. You may specify any number of extra headers and use the option multi time. Note that if you should add a custom header twice , your second option set header will be used instead of the first. you can use this option such as -H "key1:value1,key2:value2"'
queries_help = 'list of tuples to send in the query string, this option is similar to header and you can use it such as "key1=value1&key2=value2'
data_help = 'Sends the specified data in a POST request to the HTTP server. This will cause PyCurl to pass the data to the server using the content-type application/x-www-form-urlencoded. If the header content-type set to application/x-www-form-urlencoded, you need to send params as "k1=v1&k2=v2", otherwise you will see a warning message.'
json_help = 'Sends the specified data in a POST request to the HTTP server as JSON. This will cause PyCurl to pass the data to the server using the content-type application/json. If the header content-type set to application/json, you need to send params as \'{"k":"v","k2":"v2"}\', otherwise you will see a warning message.'
file_help = 'You can send specific file by this option, you must send the file like "filename:filepath". you can use absolute path or relative path. This will cause PyCurl to pass the data to the server using the content-type application/octet-stream. If the given file is not exists you will see an exception.'
timeout_help = 'Maximum time in seconds that you allow PyCurl\'s connection to take. This only limits the connection phase, so if PyCurl connects within the given period it will continue - if not it will exit.'
