# Docker Concepts

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
- While running a new Docker container, we can assign the port mapping in the docker run command using the -p option:
```sh
docker run -d -p 81:80 --name httpd-container httpd
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