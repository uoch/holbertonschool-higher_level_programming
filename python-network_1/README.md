Python - Network #1

Certainly! Here's an overview of the commonly used functions available on the response object returned by urllib.request.urlopen:

- response.read(): Returns the response body as bytes.
- response.decode(encoding): Decodes the response body using the specified encoding.
- response.getheader(header_name): Returns the value of a specific header.
- response.getheaders(): Returns a list of all headers as (header, value) tuples.
- response.status: Returns the HTTP status code of the response.
- response.reason: Returns the HTTP status reason phrase of the response.
- response.geturl(): Returns the URL of the response.
- response.info(): Returns an instance of the http.client.HTTPMessage class that contains the headers of the response.
- response.getcode(): Returns the HTTP status code of the response (same as response.status).
- response.isclosed(): Returns a boolean indicating if the response is closed.
- response.fileno(): Returns the file descriptor of the response.
- response.readable(): Returns a boolean indicating if the response is readable.
- response.readline(): Reads and returns the next line from the response.
- response.readlines(): Reads and returns all lines from the response.
- response.seek(offset, whence=0): Changes the current file position within the response.
- response.tell(): Returns the current file position within the response.
- response.writable(): Returns a boolean indicating if the response is writable.
- response.write(s): Writes the given string s to the response.
- response.writelines(lines): Writes a list of lines to the response.
These are some of the commonly used functions available on the response object. You can refer to the Python documentation for the http.client.HTTPResponse class (https://docs.python.org/3/library/http.client.html#httpresponse-objects) to explore all the available functions and their usages.