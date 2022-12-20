# Docker Swarm

At its core, Swarm is actually a server *clustering solution that brings together different operating systems or nodes into a single manageable unit that would allow us to orchestrate the containers*. <br />
Following points may be more helpful to understand it better:
- Docker in itself is not just *container runtime*. It is more than that, thanks to Docker Swarm that came out in 2016.
- Swarm is actually an in-Docker container orchestration service. It is a clustering solution built within Docker itself.
- Swarm's existence brings forth the concept of orchestration which is actually fundamental in the understanding of the real-world use case of containers. Because containers come with a lot of nuances and problems as well when they are used in production. Swarm manages all those issues and allows their coordinated operation. This is what orchestration means.


## Motivation of Docker Swarm

With the shift in major software components to Docker's container model, there comes the question if it would be able to handle everything efficiently at all. This problem arises because there is too much of reliance on containers these days. So how do we ensure:
- Containers dynamically scale in and out with respect to the traffic?
- Containers store and manage data (secrets or passwords or other important data) upon replication?
- Containers can get replaced without downtime in case of health issues?


## Limitation of Regular Docker

The `docker run ...` command did not have the ability to start a whole bunch of containers at once in a coordinated manner. <br />
The `docker service ...` command does just that, enabling heirarchial architectures.


## Basic Concepts

It is worth realizing that when we deal with Swarm, we should take away the bare concepts of concepts of Docker and abstract it away by imagining them being orchestrated by the Swarm architecture. It is important that we treat the container as cattle instead of individually catering to them. Because that is the job of Swarm. Our job is to just make the configuration work. The rest is Swarm's headache. <br />
This means, we don't really need to spend time in figuring out container names or container configurations individually. Swarm mans them.
- **Manager Nodes**: In a Swarm architecture, there are manager nodes. Their job is to manage the worker nodes. They have a database on them locally, called the Raft Database. All the managers share the same copy of the database (so there is only one database). They decide where the replicas (if any) exist.
- **Worker Nodes**: Worker nodes are managed by the managers and are responsible for doing all the work with respect to the application. Manager nodes may themselves be worker nodes as well. *Default workers are not privileged to have Swarm commands run on them*. That is a privilege only the manager node can enjoy.
- **Leader Nodes**: The node that starts up the whole cluster and is generally the first member is the leader. It has manager node status by default.
- **Raft Database**: It stores the configurations and all the permissions and authority that manager nodes need to have to be able to manage the workers.
- **Control Plane**: Orders get sent around the Swarm architecture from managers to workers (or wherever) using the Control Plane.
- **Tasks** or **Replicas**: The number of replicas a particular service is given.


## Initializing Swarm

When we use the command to initialize Swarm, a lot happens within a second of teh service getting activated:
- Join tokens are created.
- Certificate for the first manager node is issued.
- Root Signing Certificate is created for our Swarm.
- Raft Database is created. No need for additional configurational databases like `config.db`, etc.


## Reconfiguring Services

The design goal of Swarm was to make orchestration possible without the need to redeploy architecture and incur downtime. So, we have the provision here to update the services on the fly without the need to worry about downtime. <br />
The commands to make the changes have been listed out in the `commands-overview.md` file. t is done using `docker service update` command. The possible scenarios of updating the services (and a lot more are possible as well):
- Alter replicas within a service.
- Include parallelism.
- Rollback service to previous configuration.
- Set username or UID.
- Add or update secrets on the service.


## Joins in Swarm

Swarm treats a machine as a separate node (which is the whole point of a node to exist - it is different machine or server, not a container sitting in the same machine). <br />
Hence, it is important for a Swarm cluser to have multiple nodes, the machines (nodes) acknowledge and willingly join a Swarm as a worker. The `join` command exists for this reason.


## Examples

1. **Setting Up a Three Node Cluster**: Refer to the `three-node-cluster.md` file.