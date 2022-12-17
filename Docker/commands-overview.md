# Docker Commands

The most important thing to note about Docker commands is that starting from 2017, Docker realised that there are far too many commands and a lot of them have multiple functionalities. So a supergroup of Management Commands were created that enumerated the resource that is to be dealt with when a certain command is being used. For example, the classical way of spinning up a container was to use `docker run`. The modern way is to be more explicit in stating what to do, so we use `docker container run` if we are to spin up a container. <br />
The set of commands used generally are:
- `version`: Shows details about the Docker mechanism within the Docker Server and Client.
- `info`: Shows more info regarding the plugins and context, et cetera. 
- `pull`: Pulls from the Docker hub an image that we want to use to make containers out of.
- `run`: Start up a docker container. If a container needs an image that doesn't exist on the machine, `pull` is automatically called.
- `ps`: Show all container processes.


## Miscelleaneous

- `docker login`: Used for lgging in to Docker. Used for accessing services like container repositories. It is important to know that the credentials are actually stored on our machine post login as a JSON. We need to logout of machines that we don't trust when we are done.
- `docker logout`: Logs out of Docker account.


## Network Commands

- `docker network ls`: This lists down all the available networks. By default, we have 3 - the bridge network (default), the host network and a `none` network.
- `docker network inspect <name>`: Shows all properties and related data about that network.
- `docker network create <name>`: Creates a network with given name. Many other properties are configurable.
- `docker network connect <network> <container>`: Connects a container to a network with given name. Doesn't automatically disconnect it from anything.
- `docker network disconnect <network> <container>`: Disconnects a container to a network with given name. 


## Image Commands

- `docker image ls`: Shows all the images.
- `docker image inspect`: Return the JSON *metadata* about the image, not really the binaries or any other data.
- `docker image history <imagename>`: Shows the image history of how the layers got altered or added in the construction of the actual image.
- `docker image pull <imagename>:<tag>`: Downloads from Docker Hub the given image.
- `docker image push <imagename>:<tag>`: Commits an image to Docker Hub. We need to tag to push, however.
- `docker image tag <originalimagename>:<tag> <newimagename>:<tag>`: Assigns the pre-existing image with a new tag (as well as a name, if desired).
- `docker image build -t <imagename> .`: Build an image out of the Dockerfile in this directory.
- `docker image build -t <imagename> -f <dockerfilename> .`: Build an image out of the Dockerfile in this directory with a custom Dockerfile name.
- `docker image prune`: This would clean up dangling images.
- `docker system prune`: Cleans up all the images.