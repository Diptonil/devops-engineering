# Connection Pooling

A common scenario in databases is having multiple clients but having limited number of connections per instance. In such a case, pooling helps by providing a centralised interface that can handle connections without the overhead of constantly creating and closing them after each query/ request.


## Traditional Method

The classic way of doing things in the backend is to write code that opens up and closes a TCP connection of the web server to the database for query execution. This is done everytime a request is made to the API.


## Pooling

- Modern day frameworks almost always take care of pooling by themselves by abstracting away the difficulties in doing it.
- When we are using pools (especially in remote or Cloud databases), our queries may improve by 50% and even more time reduction as compared to not pooling.
- The idea is to, instead of doing and open and close with the connection to the database at each request, we create a pool object outside the request handler and remove the open and close statements. This makes the connection persist.
- We can also specify the maximum number of connections that a pool can handle. As a client, we would need to wait until a timeout in case the maximum connection limit has been reached.
- We also have *idle timeout*, which means how long whould a connection persist even if nothing really is going on.
- We have *connection timeout* that disconnects a connection after a certain time has passed, regardless of the data transfer.


## Any Cons of Pooling?

If an application essentially opens up a connection and leaves it open, we may have resource leaks and staleness in resources. <br />
In short, there is no noticeable con to this since pooling mostly is self-maintaining and almost always improve performance.