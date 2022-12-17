# Docker

Docker is a software that is built around the idea of *containers* to optimise and reinvent new developer workflows. A container is like a system with a whole different environment and a unique namespace that utilizes a certain set of physical memory resources to maintain that environment and run a certain application within it without interrupting with the external workflow of an OS. This type of definition might seem very similar to that of a VM. <br />
The dissimilarity between the two is that containers can run within VMs to streamline processes of having an application deployed somewhere. It is low on resource demand as compared to VMs and are used to manage dependencies and requirements for a particular application to run more effectively. It can also be distributed among others globally.


## Need for Docker

There are three key things that was kept in mind while making Docker:
- **Isolation**: Before VMs had come into the picture, every server was loaded with certain packages and libraries with specific versions that could just support one use-case. This led to unnecessary sharing of file systems, ineffective use of resources and large costs. Compartmentalization was not happening due to which the servers were brittle. <br />
Post VMs, the problem seemed to be that there were too many VMs around. Managing so many VMs was a hassle because one VM was doing something that would be quite similar to some other VM that would need to be spun up just to utilise the service with a few more nuances. The number of stray VMs like these needed to be reduced. <br />
With containers we reduce the host count, the OS licences, etc. A different version of the same app without any conflicts can be run on the same machine with no conflicts.
- **Environments**: Separate file systems, separate namespaces, ability to scale (using k8s), ability to run concurrently, etc. makes Docker perfect for shipping softwares with less problems with the environments.
- **Speed**: If the points above are managed, with respect to software lifecycle, we can easily say that we have extreme speed in terms of development, testing, shipping and managing.


## Primary Components

There are many components to the whole system. The ones to focus on are (the first three make for Docker's utility to *build*, *ship* and *run*):
- **Docker Images**: Quite simply, it is a universal package manager that is language agnostic, cross-platform and is able to run on all machines. The `docker build` command is used to build images.
- **Docker Registry**: It is known as the OCI Distribution these days. It is the platform from where Docker Images can be shipped and acquired. It can be compared to the GCP Marketplace or the PyPi platform. There are many registries out there namely `docker.io`, `quay.io`, `ghcr.io`, etc. The `docker push` command is used to push images to Docker Hub. This command packages the image and sends it over and makes it available publicly. To use this image, we use `docker pull` command with the name and tag of the image that we actually would like to pull.
- **Docker Containers**: They are isolated environments that get spinned up using the base template of an image. Comparing with concepts of OOP, if images are classes, containers would be objects.


## Docker Client & Server

When we run `docker version` to check installation, we are greeted with two sections of output logs - the client info and the server info. The client info is always accessible. The server (Docker Engine) info can only be accessible if the Docker Daemon (more on that later) is running. When we have Docker installed on our system, we might access the Docker Engine (server) by either *sockets*, *SSH tunnels* or *TCP/TLS*. In general, if we run Docker Desktop on our system, obviously that makes our computers act as both client and server. <br />
The outputs for both should be the same apart from the OS (maybe).


## Docker Images

They are templates that have different types of dependencies, packages with varying versions, libraries, binaries and layers packaged together so that they can be used to create containers that do a specific job. Simply put, it is *the application that we want to run*.


## Docker Containers

It is the *instance of an image running as a separate, individual process*. When a container runs, a lot of things go on inside of it. There are many ways to know that:
- `docker container top <container>`: This lists all the processes actually running inside the container. These process are nothing but tasks that get spawned as a result of the executing of a certain command.
- `docker container inspect <container>`: We get a lot of metadata as well as usable data about how the container started in JSON form.
- `docker container stats <container>`: We actually get to see the physical resource consumption of the container (or all containers if the field is omitted). In production, we would of course use far more sophesticated tools like Prometheus or Grafana. This is suitable for low-level inspection as well as learning and testing. 


## Useful Resources

1. `labs.play-with-docker.com`: This website is used as a testing ground to play around with Docker. It provides a CLI with an instance running within which we can practice working with Docker and run few commands and test out how things work.
1. `Visual Studio Code`: This IDE (as well as `Vim`) are a favourite in the DevOps sphere. A lot of extensions make life easier while working with. They are:
    - Docker
    - Kubernetes
    - Remote Development (and its other extensions)


## Contents

This section of the repo consists of multiple important concepts that are relevant to gain mastery over Docker. It is recommended to go in this order:    
- **Containers**
    - Working With Nginx
    - Container Concepts
        - Container Names
        - Detachment
        - Port Mapping
        - Environment Variables
        - Networking
    - General Information
- **Images**
    - General Information
    - Docker Hub
    - Dockerfiles
    - Dockerfile Size Optimization Techniques
- <a href="commands-overview.md">Overview of Docker Commands</a>
    - Network Commands
