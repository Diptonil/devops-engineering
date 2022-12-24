# Microservices

To understand the Microservices architecture, we need to revise everything that is wrong with Monoliths.


## Monolithic Architecture

Before Microservice Architecture was introduced, the Monolithic architecture was used. In a monolith, *the whole application code is part of one bundled unit*. For example, if we are developing an application for a Shopping Cart, the payment service, the notifications, program core logic, user authentication, etc. would all be a part of one single unit. The features of this are:
- To scale up the app, we would have to scale up the entire unit. 
- App has to be deployed, scaled and developed as a single coupled unit.
- Only one tech stack to be used to write the app.
- Teams must coordinate well since every functionality that they work on are ultimately closely coupled with all other features.


## Cons of Monoliths

- **Difficult Team Coordination**: There was always the issue of introducing features that resulted in code breakage and bugs.
- **Scaling Entire Architectures**: Higher infrastructure costs would be incurred if the entire monolith is scaled out when only a part of the application is incurring traffic.
- **Version Dependencies**: A part of the software might be built using a version which may be using a dependency of some other version as to what is being required by the other parts of the application. Such conflicts are hard to resolve in monoliths.
- **Testability**: Testing suffers because introduction of a feature might bring down another functionality and make all tests fail.
- **Longer Release**: CI/CD processes take way too longer.


## Microservice Architecture

All problems of Monoliths were solved if all the different components in the application were broken down into independently functioning systems. Microservices are *single, independently usable units that are derived by breaking up a large application into many smaller services*. <br />
Such an adoption begs the questions as to how to break down code, or how to make the microservices communicate to each other? The division must be corresponding to business needs and not technical needs. For a Shopping Cart app, the microservices would be: Users, Products, Payments, Checkout, etc.


## Features of Microservices

- Services should be loosely coupled.
- There should exist one microservice for one functionality.
- Microservices must not be dependent on each other.
- Every microservice should have versions and should be developed, scaled and deployed independently.
- Microservices can even be developed using different programming languages. Every microservice is free to choose its own tech stack.


# Communication Among Microservices

Every service would, obviously, require something from different services. There are many ways for communication:
- **API Calls**: Every service would have their own endpoints. They would be running separately and to communicate, data would be sent as requests or responses to the endpoint that needs to be communicated with. This process is synchronous.
- **Message Brokers**: There exist Publisher Services who want to send data and Subscriber Services who would recieve the data. The Message Broker itself would be a queue data structure that would replay the message.
- **Service Meshes**: This technique is more particular to Kubernetes and shall be dealt with later.


## Cons of Microservices

We note that by making an app run with microservices, we are effectively making our application a distruibutes system, something that comes with its own price.
- **Configure Communication**: This is an added overhead that monoliths did not have.
- **Increased Management**: To keep a check on which microservices are consuming how much of resources, how many are healthy, etc. we need more management than monoliths.
- **Code Management**: Managing code with relations to other codebases is difficult at times.


## Code Management

Monoliths have the simple option of using a version control repo using GitHub. But we have Monorepos and Polyrepos for Microservices.
- **Monorepo**: This means having only one Git repository for multiple services.<br />
Pros: Only one repo to clone and manage, overall simplicity, shareable materials like Manifests, Charts, etc. are handled easily.<br />
Cons: Microservices inevitably become tightly coupled, slower Git interactions, only one pipeline for one repo (this means configuring pipeline more intricately to ensure only parts of our application getting deployed).
- **Polyrepo**: This means having multiple Git repositories for multiple services. GitLab is especially geared towards providing a very impressive platform for Polyrepos by having Groups in which variables and secrets can also be shared.<br />
Pros: Teams are unbothered by unnecessary code changes, no risk of work interference. <br />
Cons: Switching between projects is tedious, cross-cutting is difficult, resources like Manifests, Dockerfiles are tough, testing and debugging becomes very difficult.
- General Rule: Go for Polyrepos if code isolation is required, there are separate teams and a large application is being built. Stick to monorepos if smaller projects are being made.


## Tools

One of the major provider of tools to work with Microservices is a platform called **Hashicorp**. Their services range from security to infrastructure and application. Their tools are becoming a standard in this field, in conjunction to container orchestration technologies like **Kubernetes**.