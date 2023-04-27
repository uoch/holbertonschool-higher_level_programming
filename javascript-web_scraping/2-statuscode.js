#!/usr/bin/node
/*    response.headers: an object containing the headers of the response.
    response.body: the body of the response, which could be a string, a buffer, or a stream, depending on the options you used to make the request.
    response.request: an object containing information about the original request that was sent, such as the URL, method, headers, and body.
    response.statusCode: the HTTP status code of the response, such as 200, 404, or 500.
    response.statusMessage: the HTTP status message of the response, such as "OK", "Not Found", or "Internal Server Error".
    response.elapsedTime: the time elapsed between sending the request and receiving the response, in milliseconds.
    response.request.headers: an object containing the headers of the original request.
    response.request.method: the HTTP method of the original request, such as "GET", "POST", or "PUT".
    response.request.uri: an object containing the parsed URL of the original request.
    response.request.body: the body of the original request, if any.
    */
const request = require('request');

const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
