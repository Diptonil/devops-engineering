# Proxy

These are servers (actual machines) that act as the middleman between the client and the server.


## Proxy Server

A proxy server is a machine that impersonates as the client when a communication is happening. Data first goes to the server from the client through a proxy. The proxy then forwards the request to the server. And all that the server knows is that the client was the proxy, rather than the actual client.


## Kinds of Proxies

There are many variants of the proxy server. They are:
- **Anonymous Proxy**
    - This doesn't make use of an original IP address. This provides a higher anonymity than the regular ones, although these services are still detectable.
- **High Anonymity Proxy**
    - This proxy cannot be detected as a server being used as a proxy.
- **Transparent Proxy**
    - These types are suited for caching because they don't have the feature of masking original IP, in fact it shows the original IP. The only use is caching here.
    - Also known as Inline, Forged and Intercepting Proxies.
- **CGI Proxy**
    - They are rarely used now and were used to make websites more accessible. They accept requsts to target URL using a web form, processes it and returns the result to a web browser. So it isn't really doing a lot and is indirectly just making more hassle than solving it.
- **Suffix Proxy**
    - It appends the proxy's name to the URL to the content being accessed. It is used to bypass web filters but these days they've become useless due to the sophestication of the web filters.
- **Distorting Proxy**
    - Once being detected as a proxy server, they use an incorrect IP address to denote the client, thus misleading the server.
    - HTTP headers are used to maintain client IP address confidentiality.
- **TOR Onion Proxy**
    - It is software that aims at online anonymity to the user’s personal information. More detailed discussion would be out of scope.


## Need for Proxy

- **Caching**: Proxies can be even used to cache things. Once a material loaded is cached in the proxy server, the request doesn't need to be forwarded to the actual server anymore.
- **Anonymity**: The main server would never know where the actual origin of the request is, as long as a proxy is used.
- **Block Websites**:
    - Many ISPs use Proxies to disallow the users of their networks to access some websites or applications. It might be for various private or government reasons.
    - Many organizations use proxies in their networks to disallow use of leisure websites or such by the employees during work hours. It can also be used to protect the employees from mistakenly accessing content that might interfere in their confidentiality.
- **Logging**: A proxy server stores the logs that are generated with respect to the requests and responses that occur.
- **Microservices**: A sidecar proxy is a common use-case here. They would be responsible to take a very primitive request and apply fancy configurations to it to make it behave in a certain manner.


## Reverse Proxy

- It is the opposite of a regular proxy. There, the server didn't know the client. Here, a client doesn't know the server.
- So, when a request lands on a reverse proxy, it directs it to the actual servers out there. So, the server's address known to the client was actually not the actual address. This whole thing indeed is load balancing; it is up to the reverse proxy server to direct those requests to the server as it deems fit.


## Need for Reverse Proxy

- **Caching**: It comes here again. The request doesn't have to travel to the backend. It can get resolved in the reverse proxy itself, provided the materials are cached.
- **Load Balancing**: The use case is already detailed.
- **Ingress**: It is actually the features used in container orchestration where the reverse proxy is responsible for looking at the requests and funneling it to the servers actually responsible for executing those requests.
- **Canary Deployment**
- **Microservices**


## Types of Proxy Server Protocol

- **Socks Proxy Server**: This type of proxy server provides a connection to a particular server. Depending on Socks protocols, this type of server allows the multilayering of various data types such as TCS or UDP. This is a very low-level proxy.
- **FTP Proxy Server**: Using the concept of relaying, this server caches the FTP requests' traffic.
- **HTTP Proxy Server**: For use with the HTTP.
- **SSL Proxy Server**: This type of server was developed using the concept of TCP relaying being used in the SOCKS proxy protocol to allow Web Pages’ requests.


## Questions

- **Can proxy and reverse proxy be used at the same time?**
    - Yes, in Service Meshes. It is a concept more geared towards microservices and Kubernetes.
- **Can a proxy be interchanged for a VPN?**
    - VPN is technically more secure than a proxy because they are more low level than the default implementation of a proxy. So, the only thing a VPN can see is the domain that is being visited, nothing else. This is not the case with a proxy.
    - A TLS-type Proxy can see pretty much everything (as with all of them, alomst).