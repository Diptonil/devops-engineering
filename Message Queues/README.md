# Message Queues

A message queue provides a lightweight buffer which temporarily stores messages, and endpoints that allow clients to connect to the queue in order to send and receive messages. The messages are usually small, and can be things like requests, replies, error messages, or just plain information. It can have the potential to greatly relieve a server from being overburdened and promote the principle of separation of concerns in system design.


## Without Message Queues

In a client-server architecture, whenever a request is fired, there is a finite amount of time that the server is allowed to spend to fulfill that request. That request can range from something very minute to something very load-engaging. Different servers employ different techniques and technologies to work through it. Some servers use multithreading, some servers use asynchronous single-threading, etc. But whatever approach a server decides to take, at times, the number of request and their demands might just not let the server-side optimizations cut it. <br />
Hence, the cases of a *lot of requests coming in* that cause a congestion or *requests that just take too long to process* (again, causing congestion), are the reasons why there would be a lot of requests just dangling around to either make a TCP connection or get a valid response or be acknowledges, etc. <br />
This is harmful even for the UX because users hate to not see anything upon interacting with the website.


## Ineffective Alternative to Message Queues: Horizontal Scaling

One way to address this solution is horizontal scaling: get a reverse proxy, segment the incoming traffic to swizzle into different nodes of the website by acting as a load balancer. <br />
The reason why it is **somewhat ineffective** is because requests that lead to significant processing at the server. This means, no matter how many servers we spin up, each server again gets hooked up to a long-processing request that would take a lot of time, thereby blocking that server from other requests, yet again. This just irrationally increases costs without offering much optimizations.


## Solution Using a Queue

Having a queue offers the benefit that whatever request comes in, it immediately gets queued by the server. The whole operation takes O(1) time (enqueing). And spontaneously, the server responds to the client back with an identifier that acknowledges the request. It doesn't guarantee the execution of the request, but doesn't keep the user waiting. <br />
It is better for the user to know that something is happening instead of not having their requests acknowledged.


## When is Queue a Better Option?

- When the processing time of most request to a service starts to become indeterministic, go for queues.
- If the requests to the backend are very resource hungry (for whatever reason), it is a bad idea to have just the web server deal with everything out there. *A web server is a machine that serves web with responses*. Just taking the request and responding should be its only job. No processing, no calculations, etc.