# Docker Container Concepts

This file contains all relevant and important concepts that are ecessary to be understood to take full advantage of the app and be able to seamlessly work with it.


## Container Names

- Docker is required to pick a name that is unique in our systems. That name can be issued by us (using '--name') or will be generated randomly for us. Docker does this by picking out adjectives and names of scientists or hackers from an open-source list. The combination results in: 'adjective-name'. These randomly generated names also let us see how the containers should be named conventionally.
- Naming is always recommended because it helps to refer to containers without the IDs (which is a pain because of the long numbers).


## Detachment

This is the process of letting a container run in the background. Oftentimes, we need to work on a single terminal on a lot of different things. And we would want a certain operation to continue running in the background without allocating a terminal specifically for it. Detachment is the way to go.
- The '-p' flag is responsible for detachments.
- Using ^C instead of using detachment might mean the stoppage of containers (in Windows it might happen differently).


## Port Mapping

If we want to communicate with a Docker container from our host machine, we need to have a port mapping. Port mapping is used to access the services running inside a Docker container. We open a host port to give us access to a corresponding open port inside the Docker container. Then all the requests that are made to the host port can be redirected into the Docker container. Port mapping makes the processes inside the container available from the outside.
- The '-p' flag is responsible for mapping ports.
- While running a new Docker container, we can assign the port mapping in the docker run command using the -p option (host machine port 81, container port 80):
    ```sh
    docker run -d -p 81:80 --name httpd-container httpd
    ```
- When we have a container ready and would like to know more about their ports, we run:
    ```sh
    docker container port container_name_or_id
    ```
- The above statement would enable us to connect to the container from our machine. The `httpd` server in the container listens on port 80. The host's port 81 is connected to the port 80 of the container now.
- This means that we can access the application spawned by the container on port 81 of our machine. We can hence route traffic from the Docker client (our host) to the Docker server (the container that is being run). We get a HTML reply of something like 'it works' if we execute this:
    ```sh
    curl http://localhost:81
    ```
- It is *not a mandatory feature*. At times it can be quite useful.
- Three ways to do it *after a container has already been started and worked upon*:
    - **Relaunch a container with the command that maps the port from image**: Very straightforward and basic. However, we will lose all changes that had happened in the old container. We can prevent data loss and still proceed with this method if we use Docker Volumes but that altogether becomes quite messy.
    - **Using Docker Commit**: We can commit the old Docker container to create a new Docker image and use that to start a new container with the right ports open. We would stop the container and create an image out of it. And then we remove the old container. Then we start up a new container with the image that we just generated.
    - **Altering config files**: Although the container works the same way, its metadata is completely different from the previous one. This process deals with modifying the existing Docker container instead. This can be done using the config files.


## Environment Variables

It is common to pass certain environment variables during the starting of a container. These variables may be used for a variety of purposes within the container process. The use of these variables could be written in a Dockerfile as well.
- The '-e' flag is responsible for signalling the passage of an environment variable.


## Interactive Mode

We can interactively work with our containers as well. In examples of running web servers like Nginx or Apache, we would not have needed to run a shell in the container but at times we may need to do that. For that, we run the interactive mode.
- The '-t' flag allows to make a TTY connection (similar to SSH) into the container.
- The '-i' flag allows to maintain and hold the connection thus established.
- Containers running like that should have a final configuration: running the `bash` command over the default image command. This is done by writing out the command to start the container and finally appending the command that is to overwrite the default command.
- Images like Ubuntu or any other OS have the `bash` set as the default. So we don't need to do this for those containers.
- Not all images may have `bash` installed or packaged with them (the Alpine image). In that case, we would get errors. A simple solution is to start up the Shell by writing `sh` instead of `bash`.
- We use `exec` instead of `run` if we wish to interactively start an existing container.


## Virtual Networks

The idea of a virtual network is that every container in a network may connect with each other without needing to know the port (-p flag). This means, *ideally*, it is best for us to club all related containers in a single network (if we are doing something with microservices using Docker Compose and have an API Server and a database that needs to talk to the server (and more such situations)).
- By default, each container is assigned an IP different from the host machine. We can know that IP by:
    ```sh
    docker container inspect --format "{{ .NetworkSettings.IPAddress }}" container_name_or_id
    ```
- The default virtual network is called "Bridge" or "docker0". When we do port mapping, it isn't the port *of the container* that recieves the traffic, it is the port of this network that gets interfaced with the network of the host machine.
- The "Host" network is the one that can be used in case the step of networks is not needed. In that case, the containers get attached to the host machine's network. This scarifices a lot of security but might be something that we need in certain cases. No ports need to be mapped.
- The "none" network is more like a placeholder. It doesn't really have a network to be attach to. It is used when networking (in any form) is not needed.
- While creating containers, we specify networks as:
    ```sh
    docker container run --network bridge some_image
    ```
- If we already have containers running but we'd like to switch networks, we would:
    ```sh
    docker container connect <network-name> <container-to-be-connected>
    ```
- Containers attached to the same network may ping each other. Inter-communication between containers on a same network is done by DNS that we can use in custom networks. We cannot really go for the method of IP addresses since they may change. Given names don't, however.
- It is recommended to always go for custom networks instead of using the default. Docker Compose makes networking much easier when multiple services belonging to the same application comes into picture.


## Persistent Data

Containers are usually immutable and ephemeral. This means that the data that they generate, upon their exit, gets erased. There is no way to maintain that state within them. Hence, they are *stateless*.
Hence, we need a way for containers to have some degree of persistence when we want them to. This can be done using two options - *Volumes* and *Bind Mounts*.
- **Volumes** are storages that are special locations *outside* the container's UFS (union file system). They create folders on the host machine that stores the unique data generated by the container.
- **Bind Mounts**: These link a container path to the host path.


## Volumes

The concept of volumes at a glance might seem easy enough but there are certain nuances to it. The whole point of a volume is saying that data contained within it is way too important - more than the container itself. So, deletion of a volume is a manual process (which is just for insurance).
- Generally, volumes are reserved and belong to the Docker architecture. Every created volume goes straight to a designated path by Docker that we cannot change (we can define our own paths in Bind Mounts).
-  Multiple containers can run with the same volume when they need access to shared data.
- We can be sure that would need to attach a volume to a container if the term `VOLUME` is mentioned in the Dockerfile of the image that we would use. No matter how we decide to use volumes in our container configurations, the `VOLUME` clause would be there for images that require volumes.
- While we create containers, if we do not explicitly mention the name of the volume, a long, unreadable ID is produced. While this is quick and easy and might be something that gets the job done faster (and can certainly aid more experienced people), it is recommended to be explicit about naming the volumes whilst containers are created. That can be done when the `docker container run ...` command is executed with the `-v` flag.
- Sometimes, we would want to create a Docker Volume (not really belonging to any container yet) way ahead of time for use later. We have the `create` command for that.


## Bind Mounting

It is the process of mapping a host file or directory to a container file or a directory (basically just two locations pointing to the same file). This skips UFS and hence the container may overwrite host files.
- We do not need any Dockerfile command for this. This is done during `container run`. Bind Mounts don't require a `VOLUME` clause (it can be there as well - doesn't make a difference, really).
- Bind mounts, unlike Volumes, start with a forward slash.
- It is completely a configuration done from the side of the host. It is generally meant to copy over the contents of a certain part of the container's internal file system over to the specified path of the host.
- Primarily, when the container is running, *any change made to the host directory set as the mount would reflect in the container and vice-versa*.
- To summarize, *whenever we need a scenario in which we want the container to behave dynamically with respect to changes made in the host system, Bind Mounts are the way to go*.