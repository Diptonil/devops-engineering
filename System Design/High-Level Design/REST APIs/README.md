# REST APIs

It stands for Representational State Transfer. The central idea here is the representation of entities. At the core, REST is nothing more than *a convenient specification of how clients should demand for data and how servers should respond to the requests made by the client*. It is just a suggestive framework. It is not an enforcement. <br />
Everything in REST is a *resource*. These resources are generally coded in form of JSON these days. For example, for an e-commerce website, teh resource can be any item in the data base (any product, user or order, et cetera).


## What REST Does Not Tell Us

- REST specifies how the data should be interfaced to the clients. It dictates the way a client should be responded to. That's all it says.
- REST doesn't enforce us to *store* the data in our databases in a particular way or format. It doesn't tell us to store it in some rows or whatever columns or to use a SQL or a NoSQL database. 
- This means that a client may ask for data in a particular way in which it expects a response. It is unbothered with how it is being stored or fetched. 


## Representations

We have two types of representations:
- *Internal Representation*: This deals with how we choose to store and represent data in our storage and databases. This doesn't deal with how clients are served and is purely internal.
- *External Representation*: This deals with how the responses are stuctured and in which format (XML, JSON, et cetera). And this what the clients come across.


## CRUD

Every endpoint that is capable of being accessed *acts upon a resource*. This resource is mostly specified in the endpoint itself. The operations that can be requested can be any one among the CRUD operations. The request would typically have the corresponding verb like for retrieval, GET. For updation, PUT. For deletion, DELETE.


## Common Principles

- **It is a specification, not a protocol**: It works on top of a protocol. It can be implemented over any protocol. For optimality, though HTTP(s) is chosen. They have very agreeable compatibility.
- **Gels very well with HTTP**: So much so, they have become quite synonymous. We might even be just exposing simple HTTP endpoints over a server but might think that we are making a REST API. Reasons why they work together so well:
    - HTTP verbs are similar to the REST endpoints. The endpoints identify the resource and the action together.
    - For an endpoint, multiplexing is possible. By that, it means that an endpoint can handle a POST, GET, etc. requests at once. It's not that an endpoint can handle only one operation at once. This makes for simpler and more cohesive programming.
    - Has a very efficient tooling (refer below).
- **No Need for Verbs in Endpoints**: We do not need to create endpoints like `/create/resource` or `/edit/resource`. We can just do `/resource`. We can design all the corresponding requests programmatically.


## Tooling

We have very extensive set of tools that we may use to leverage advantages of gelling HTTP and REST together:
- **HTTP Clients**: Postman, Request library for Python, cURL, etc.
- **Web Caches**: Nginx, Varnish, HA Proxy, Apache
- **HTTP Monitoring**: Tracing, Packet Sniffing, Alerting
- **Load Balancers**: Distribute load uniformly
- **Security**: SSL
- **Compressing and Optimizations** <br />


## Downsides

Most of these downsides could be easily solved by RPCs.
- **Consumption is not easy**: Using this is not as easy as just making RPCs. We would need an HTTP client to make requests and get responses. We first need to convert it to native objects and then consume it. There is no native language that is absolute to make things easy (like RPCs).
- **Less Standardization**: The endpoints may be named in any manner. there exist very less rules that strictly define a standard to write endpoints. Sometimes, this leads to sub-standard endpoint names.
- **Some webservers may not understand all HTTP verbs**: Some web servers that we choose to use (for whatever use-case) may not support all the verbs. Servers like Nginx, Jersey, etc. are okay with it, though.
- **Consumption is Repetitive**: In the web server, the same piece of logic is used again and again with every request. This can make utilization of machines uselessly repititive for no reason.
- **Huge Payloads**: This is a common issue almost everyone runs into. Low-latency requirements may not be supported by this specification.
- **Protocols Cannot be Switched**: We can't easily switch from TCP to UDP or something similar at our ease.