# Denial of Service Attacks (DOS)

What it essentially means, very simply put, is to do a bare minimum to disable a backend system from serving its utilities. This effectively means to overwhelm a server by exhausting its hardware resources completely (memory, CPU, network bandwidth, etc.). <br />
There are many inventive ways to do it. Six of them are listed here.


## Long Running Requests

- This technique involves sending a simple request to the backend that would take a long time to execute and hence would starve the server of its resources. If multiple such requests are sent, the backend would get saturated in no time.
- One such example is the *Slow Lorris*. This involves establishing a TCP connection to the backend and sending a moderately sized request byte-by-byte. This would effectively lead to congestion since the backend would continue to listen to the full request instead of serving the other requests.
- To avoid these, watch out for particularly large requests in the backend that might overwhelm the server.


## Crash a Backend

- They're the most dangerous ones because the backend would actually get effected.
- Less work from the side of attacker is needed here. This generally happens due to vulnerabilities in backend frameworks or services (that regularly get patched).


## Exhausting Maximum Connections

- One of the maximum counts of the number of TCP connections per server node is 3 million by WhatsApp. If the attacker has enough resources or IoT devices or distributed systems to trigger certain attack at a given time, it can be possible.
- The presence of load balancers these days save some trouble. But they too are servers that route the requests. If enough number of requests hit it at the same time, there is a chance that even that might go down.


## Large Responses

- Responses are, by themselves, pretty large in default. An average size response may have a 600 kB payload, which in itself is quite huge. But sometimes it might as well be bloated to about 1.5 to 3 mB. That is plainly obnoxious. This leads to a bit of higher processing of memory resources and network bandwidth. That is undesirable.
- These bloats are unnecessary and they happen due to the frameworks and the inability of backend engineers to use them effectively or not knowing it.
- The process of trading cost with less lines of code and faster development is *leaky abstractions*. This is not what we want to build a stronger backend.
- This is one of the most troublesome issues and Ukraine in the cyberwar against Russia has faced this issue.


## Lost of Requests

- THis is different from eshausting maximum connections. That just involved making TCP connections. This involves firing multiple requests from a lot of different places. 
- Executing this is extremely sophesticated. It is not that simple. Various techniques of spoofing or disguising as the attacker is to be done to get here.
- This is the most common one.


## Complex Request

- This involve one simple request that can exhaust CPU or memory in the backend. These requests are called CPU bound or CPU intensive.
- These aren't same as returning a particularly long response (as seen in the 2nd reason) or having a particularly long request to process. The difference is that here the computation is extensive and unprecedented. 
- Examples would be requests that have complex regex or complex manual queries, etc.


## Distributed Denial of Service Attacks

This happens when any of the 6 methods discussed above is executed on a grand scale, at the same time, with a alot of machines over a distributed system.


## Prevention

- While designing APIs, watch out for requests that would take a long time to execute. Watch out for complex requests as well.
- Set up timeouts! They are very important.
- Use services like Cloudflare. Point the DNS to let them recieve traffic first so that they can survey the request first and see if it is legitimate before sending it over to the API server.