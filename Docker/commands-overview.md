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


## Container Commands

- `docker container stop <containername>`: Stops a container. Does not delete it. Its UFS still exists and is intact.
- `docker container run <imagename>`: Runs a container with the image as given. If the image is not locally found, `docker image pull` is executed first.
- `docker container run -d <imagename>`: Runs a container with the image as given in detached mode. It runs, but in the background without consuming a whole shell for no reason. We may want that sometimes. Depends on the use-case.
- `docker container run <imagename>`: Runs a container with the image as given in interactive mode. It runs and provides us with a shell that we can use to access the contents of the container. So, a whole terminal needs to be dedicated to interact with the running container. We may want that sometimes. Depends on the use-case.
- `docker container run --name <containername> <imagename>`: Runs a container that has a given name. Normally, containers are given random names. If they have names, they are easily identifiable and *rememberable* instead of having to use IDs.
- `docker container run -p <machineport1>:<containerport1> -p <machineport2>:<containerport2> ... <imagename>`: Runs a container with port forwarding. The Dockerfile of every image may have a list of ports opened up for accessing the container (one or more). We can accordingly expose a certain port of the container and attach it to the host machine.
- `docker container run -v <volumename1>:<volumepath1> -p <volumename2>:<volumepath2> ... <imagename>`: Runs a container with named volumes. The Dockerfile of every image may have a list of volumes that can be used. By using this command, we make sure that the volumes don't have some gibberish ID and are named properly.
- `docker container run -v /<hostpath1>:/<containerpath1> -p <hostpath2>:<containerpath2> ... <imagename>`: Runs a container with bind mounts. 
- `docker container exec <flags> <continername>`: The Docker `run` command is used to start a new container from an image. However, this command is used to run operations on currently running containers for purposes of examination or whatever the use-case may deem.


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


## Volume Commands

- `docker volume ls`: Shows all the volumes that are currently on the host machine. It gives the volume name (which is a huge ID) and the driver.
- `docker volume inspect <volumename>`: If we take that long ID and inspect it, we might be able to tell where in the host machine it is running as well as have some metadata about the volume.
- `docker volume prune`: Cleans up unused volumes.
- `docker volume create <volumename>`: Creaes volumes ahead of its use.


## Compose Commands

- `docker compose up`: Uses the `docker-compose.yaml` file in the current directory to set up all containers, volumes, etc and start the entire architecture described in the YAML file.
- `docker compose up`: Same as above except we wouldn't get any logs to the screen since it would operate in detatched mode.
- `docker compose stop`: Stops the architecture completely. Does not clean up.
- `docker compose down`: Stops the architecture completely and cleans up. Removes the networks and other resources.
- `docker compose down -v`: Stops the architecture completely and cleans up. Removes the networks, volumes and other resources. Docker always protects volumes by default. Here we explicitly want them removed.
- `docker compose build`: Rebuilds images that have already been made by Compose.
