# Docker Commands

The most important thing to note about Docker commands is that starting from 2017, Docker realised that there are far too many commands and a lot of them have multiple functionalities. So a supergroup of Management Commands were created that enumerated the resource that is to be dealt with when a certain command is being used. For example, the classical way of spinning up a container was to use `docker run`. The modern way is to be more explicit in stating what to do, so we use `docker container run` if we are to spin up a container. <br />
The set of commands used generally are:
- `version`: Shows details about the Docker mechanism within the Docker Server and Client.
- `info`: Shows more info regarding the plugins and context, et cetera. 
- `pull`: Pulls from the Docker hub an image that we want to use to make containers out of.
- `run`: Start up a docker container. If a container needs an image that doesn't exist on the machine, `pull` is automatically called.
- `ps`: Show all container processes.


## Network Commands

- `docker network ls`: This lists down all the available networks. By default, we have 3 - the bridge network (default), the host network and a `none` network.
- `docker network inspect <name>`: Shows all properties and related data about that network.
- `docker network create <name>`: Creates a network with given name. Many other properties are configurable.
- `docker network connect <network> <container>`: Connects a container to a network with given name. Doesn't automatically disconnect it from anything.
- `docker network disconnect <network> <container>`: Disconnects a container to a network with given name. 