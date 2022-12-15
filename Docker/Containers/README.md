# Docker Containers

As stated afore, it is the *instance of an image running as a separate, individual process*. When a container runs, a lot of things go on inside of it. It has a lot of components to it that ensures its smooth running.


## Shells in Container

The `concepts.md` file states the theory behind *Interactive Mode*. <br />
Basically, this mode allows us to connect to the container and operate a shell within it. So, it no longer "just runs" somewhere. We can execute commands inside them.


## Networks in Containers

Refer to `concepts.md` to know more about the theory of networking.
- Each container is connected to a virtual private network (like GCP's Cloud VPC) known as "bridge".
- We may choose to utilize the benefits of *Networks* in Docker but it is not at all necessary. It provides the feature with the guideline of "Batteries included, but removable". Here are all possible things that we can do:
    - Use default in all cases (works just fine unless we have specialized security or traffic requirements).
    - Make multiple virtual networks for multiple apps in a system.
    - Have one container attached to multiple or no networks (if container gets traffic from multiple sources).
    - Skip virtual networks and directly plug into host IP (not desired in most cases but sometimes helps).
    - Use different Docker network drivers to gain new abilities.
