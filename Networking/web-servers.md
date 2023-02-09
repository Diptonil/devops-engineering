# Web Servers

Web servers are basically machines that are used to host serve content over the web using the HTTP protocol. The content can be anything - HTML pages, downloadable PDFs or files, photos, JSON, etc. It is consumed by clients side machines (us).


## Content

Content can be distinguised into:
- **Static**: Unchanging files like HTML, CSS and JS files, images, video, animations, et cetera are called static content. There is no user interaction that alters the static data in the server.
- **Dynamic**: Resources or data that varies from person to person; things that come from the databases and can be altered by using CRUD operations on them.


## Working

It operated on the famous request-response cycle in which a request is made by a client that has managed to already establish an TCP connection with the server. The HTTP request is made to the resource that it needs to access with the HTTP verb (and a whole bunch of things discussed in HTTP).


## Blocking Single-Threaded Web Server

- When a TCP connection is made, the server reserves a tiny bit of memory in its systems for the socket. This is done for every connection that occurs. Hence, we can simultaneously have multiple TCP connections to the server as long as the memory is enough for socket creation.
- However, serving is another story. The whole task of serving the requests is treated as a single process with a single thread. As a result, despite the number of connections we may have, there is only one thread that can serve the requests. Hence, evaluation of requests happen one thread (connection) at a time. Obviously, this creates latencies.
- This architecture can be altered, of course. That is what Apache does by having a setting of maximum allowed threads. That would mean the maximum connections being served at a time.


## Using Apache

- The `httpd` is the Apache2 web server. To install it in Linux:
```sh
sudo apt-get install apache2
cd /var/www/html/
```
- We notice that the folder has an `index.html` by default, which is the default thing that shows up when we go to our localhost. That means everything works well.
- It might happen that the folder is, by default, not owned by us. We need to change Linux permissions (of the `html` folder in `www`):
```sh
sudo chown -R www-data: html/
cd html
```
- We can write our own html pages, place files and folder inside it to serve them.
