# Hyper Text Transfer Protocol

It is a protocol dealing with the client server architecture built on the application layer (7). It runs atop the TCP layer. It is a stateless protocol.


## Client Server Architecture

This is the model that says that there lives a server at the center and many clients around it. Exchange of information occurs between them as:
- Client sends data to the server in form of a question or just to supply data. It is called a *request*. In most of the cases, the client is nothing but the web browser we use. In other cases, some API testing tools or utilities (like Postman and cURL) can also be clients. In other cases, programming language APIs like the `requests` package in Python or the `java.net` package in Java can be clients, or mobile applications as well.
- Server sends back a *response* to fetch some data or inform about something. We have Apache Tomcat, we can write web servers by programming in Go, Node JS, Python, etc.


## HTTP Request

There are many components to the HTTP request, but we'd focus mostly on:
- **URL**: The address of a given unique resource on the Web. In theory, each valid URL points to a unique resource. Such resources can be an HTML page, a CSS document, an image, etc. This only doesn't happen when the resource doesn't exist.
- **Method Type**: There are many methods like GET, POST, DELETE that tell the server what exactly we want from it.
- **Headers**: This carries with it some metadata and things like cookie information, API keys, etc.
- **Body**: This is the JSON content of the things that are being sent to the server of it to act upon the sent information.


## HTTP Response

- **Status Code**: Things like 200, 403, 404, etc. Numeric denotion of what kind of response was yielded by the server.
- **Headers**: Same as the request.
- **Body**: The data returned by the server.


## Resources On the Web

When a particular URL is accessed with the browser, a page loads up. Every element in that page is brought into the HTML page that gets rendered with the help of HTTP. That is exactly what it does.


## Statelesness

HTTP is called as a stateless protocol because each request is executed independently, without any knowledge of the requests that were executed before it. The connection between the server and the client is lost once the transaction ends.


## HTTP 1.0

- This was made in around 1997, when RAMs had very less capacity. Therefore, to minimize expenses, after one request-response cycle was complete, the TCP connection that always has to be established was terminated.
- This meant only 1 request-response cycle, which was okay back then since the only resource that was available was the `index.html` page.
- Hence, there would be a new TCP connection with each request of whatever resource (plain HTML pages, images, etc.).
- Buffering is used here, which makes it very slow. It means that a resource is sent at once altogether. No chunks or anything. It takes time.


## HTTP 1.1

- This was made around 2015 and it added a 'keep-alive' header. This essentially prevented the TCP connection to shut down and wait until all that is needed by a page is brought in by HTTP.
- It left the concept of buffering and started streaming with chunked transfer. Loading became faster as the server doesn't need to spend too much of time loading a resource.
- It introduces the concept of pipelining, which caused more problems than the good it did.


## HTTP 2.0

- This was designed to solve all the problems that HTTP 1.1 had. It swapped pipelining with multiplexing, which means having multiple requests and kind of shoving them to be executed at once.
- It is secure by default.
- It has compression enabled.
- It also does protocol negotiation, which is basically checking and ensuring if a certain protocol may be accepted by both sides.


## HTTP 3.0

- This is also called as HTTP/2 over QUIC.
- QUIC is UDP with congestion control. So TCP is just replaced.
- Still experimental.
- Has all HTTP 2.0 features.