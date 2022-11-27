# gRPC Remote Procedure Calls

It is a modern communication framework introduced in 2015, governed by Cloud Native Computing Foundation. Like YAML, gRPC also has a recursive full-form. There are many areas that find use of gRPC, not just microservices.


## Why gRPC?

- For **microservices**, it is a special technique that is employed for communication with backend microservices. It is of great importance to note that gRPC is not responsible for much of frontend-to-backend microservice interactions, but just across all backend services in particular.
- In **general**, every application that has to access the web, due to the client-server architecture, compulsorily has to have client libraries installed for  them to work. Normally, this is not much of a deal when developing web applications since frameworks take care of the client libraries and most importantly, we have web browsers. The browser is the largest and the most extensive client library. With client libraries comes the problem of needing one that is different for every different programming language. Moreover, client libraries are hard to maintain.


## Features

- It is built on HTTP/2.
- It seeks to standardize client libraries of all programming languages by having just one usable library that can be leveraged across all languages.
- The message format is protocol buffer, which is language neutral.


## Modes

- **Unary RPC**: A simple, synchronous client-server request-response cycle. 
- **Server Streaming RPC**: A client request causes a stream of data to be delivered as a response from the server.
- **Client Streaming RPC**: A client causes a stream of data to be delivered to the server.
- **Bidirectional Streaming RPC**: Streaming of data using lockstep approach occurs both ways.