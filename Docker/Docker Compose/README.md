# Docker Compose

Softwares generally aren't created by just running one container for the whole application. A software might require the running of a lot of containers at the same time. For example, it might need to run web frontends, backend services, web servers, databases, etc. To manage and configure relationships between containers so that we can harmonize all the containers running together accordingly. <br />
There is a chance that if we could do everything like this manually in Docker as well. However, here is why using Compose can be better:
- Automation is always better than manual.
- Configurations for *all* containers written in one simple file.
- More specifications and customizations of a particular service (the application that runs in a container) in that single file than the Docker `run` command can facilitate.


## Composition

It is made up of two related things:
1. **YAML File**: The `docker-compose.yaml` file is the single configurational file that we need to use.
1. **CLI Tool**: We need to have the software `docker-compose` as we would run CLI commands using it. However, Compose comes with Docker these days and the commands have changed a bit as well. Refer to `commands-overview`.


## The YAML File

- Docker Compose has versions that needs to be specified at the beginning of the file. It is recommended to start learning from the latest versions. The concepts remain the same. Only in newer versions, we get more features.
- The default name should be `docker-compose.yaml`. But we can have anything that we want to. We would just need to use the `-f` flag.
- YAML files are heirarchial, obviously. The heirarchy here is denoted with many additions. Three primary ones are: *services*, *volumes* and *networks*.
- Every Compose file should generally have these three. We say *services* instead of containers (in this context it means the same thing, mostly) because it offers us the option to have, for each container running, its replicas. So we can scale out as and when necessary.
- Whenever we use a plural YAML key (like *ports*, *volumes*, etc.) we use the list format. In case of singular entities, we stick to the traditional key-value format. We notice that *service* and *environment* have inner lists but they don't have the dashed lists, despite containing multiple values. Note that both are singular.


## Important Clauses

- **service**: Here we define th elist of all services we would be using.
    - **image**: Here we mention the image that we are going to use for a particular service.
    - **container_name**: Here we mention the name of the container that gets spawned up to represent the service.
    - **ports**: Here we mention all the ports that we would like to open up (like we did in `run`).
    - **volumes**: Here we mention all the volumes that we would mount as storages. The left item is the volume name and the right item is the item that would get stored over to that volume.
    - **environment**: Here we mention all the environment variables in key-value pair method for that particular service.
    - **depends_on**: Specifies to Compose that a service has a dependency on some other service. That would mean that the dependent would be started after the service on which it depends starts up.


## Using Compose to Build

We can also use Compose to build our own custom images by running `docker compose up`. Doing this on resources already existing doesn't spawn new resources, though.  To rebuild, we use `build`.


## Important Points

- Certain services rely on a specific version of another service to work. It is important to make sure that all teh inter-service dependencies are satisfied for any application to work.