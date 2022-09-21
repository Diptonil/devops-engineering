# Kubernetes

Kubernetes is an open-source container orchestration tool that helps us manage containerised applications that are built with tens or hundreds of containers running inside them in different deploymwnt environments like physical machines, cloud or hybrid environments or virtual machines. It was developed by Google. It is also known as k8s.


## Need for Kubernetes

Increase in use of microservices over monoliths require all microservices to be containerised. All the containers need to be orchestrated and managed, which is very difficult to manually do.


## Features

- **Highly Available**: There is no downtime involved.
- **Scalable**: It is highly performant and can adjust itself with respect to loads.
- **Disaster Recovery**: N+Backup and restore capabilities are available.


## Components

Kubernetes has an architecture that is composed of severeal features and mechanisms, each doing something important and necessary. Such units are called components and we would be exploring them now. Example: pods, nodes, services, etc. Below we have the overview of all these components.


## Nodes

A node can be understood as an abstraction of a server that actually orchestrates all the containers. We would be running our set of containers as pods (read further below) within our node(s). Very roughly (and somewhat inaptly), we can consider nodes to represent VMs. <br />
There are generally two types of nodes in the k8s architecture: Worker Nodes (Slave Nodes) and Master Nodes.


## Worker Nodes

Worker nodes run containerized applications and handle networking to ensure that traffic between applications are managed effectively. <br />
There are three processes that must be installed within every node:
1. **Container Runtime**: The software that makes up the containers and runs it. Docker is an example.
1. **Kubelet**: The process that orchestrates the containers. It starts the pod with the container inside of it.
1. **Kube Proxy**: This is a process that regulates the smart and intelligent working and relaying of traffic between the pods within the same node or doing inter-nodal transactions. For example, Kube Proxy helps determining that a REST API app request should be sent over to a database pod within its own node (if possible) rather than bearing the overhead of going over to another node. <br />


## Master Nodes

Master node is a node which controls and manages a set of worker nodes (workloads runtime) and resembles a cluster in Kubernetes.<br />
There are four processes run by a master node:
1. **API Server**: Acts as a cluster gateway and a tool for authentication and authorization. This is the point of contact of the client with the server.
1. **Scheduler**: Upon getting requests, the API server relays it to the scheduler. It looks at the resources and decides where to run a pod in which worker node. It comes with the intelligent scheduling technique to offload tasks efficiently. It just *decides* which node to use for a pod to run. The actual running of the pod is taken care of by the Kubelet.
1. **Controller Manager**: Its job is to detect state changes like pods crashing and going out of commission and accordingly reassign then for a respawn. This request is made to the Scheduler that decides where to put the respawned pods.
1. **etcd**: Every change happening to the cluster is stored in this. This is the cluster brain. It is a key-value store. This is the point where it is determined if the cluster is healthy or not, if there had been a state change, etc. It stores everything except the application data running in the containers (of course).


## Example Cluster

- Here a very small cluster is being considered with 2 master nodes and 3 worker nodes.
- The master nodes have very less tasks to do, hence occupy less resources of the system (CPU, RAM, disk). Worker nodes actually run the containers and have higher overhead.
- As the application scales, we may need a larger cluster. For either master or worker nodes to be added, just add a server (node), install the 3/ 4 processes as described above to make it a master or a worker and it is addded to the cluster.


## Pods

- A pod is the smallest unit in the Kubernetes architecture.
- It is meant to represent a container by providing necessary abstractions over it so that we do not have to directly interact with the low-level containers and instead access the pods, that are the high-level representation of the same.
- This allows us to interact only with the Kuberenetes layer and not be worried about whatever technology we are using to run containers (be it Docker or whatever else).
- One pod is responsible to run a container within itself. The usual norm, with respect to the above definition, is one. But we can run more than one application containers within a pod (which is seldom the case).
- Each pod has its own IP address that it uses to communicate with the other pod.


## Ephemeral IP Addresses

- Pods can die while running if the containers inside them either run out of the node resources or crash due to some bugs or system overhead. In such a case, a new pod immediately spins up and the container is restarted.
- Every respawn of a pod gives that pod a new IP Address. Since the addresses aren't permanent, they are called ephemeral.
- This obviously means a lot of trouble for us in case the pods are communicating with each other for sending traffic or whatever. To overcome this issue, we use Services.


## Services

- A Service is a static, permanent IP Address that can be attached to each pod that would stick to it even if it gets respawned.
- Every single pod has its own single service.
- The lifecycle of the pod and the service is not connected in any way. So the endpoints wouldn't need to change.
- There are two types of services: external and internal.
    - External services are the ones that are made so that they can be publicly accessible (via the browser, etc.). For example, pods running suites of endpoints (REST APIs).
    - Internal services are the ones that can only be accessed privately. For examples, pods running databases.
- The service would obviously be represented using the IP addresses and the port numbers. This is something that can be undesirable when we are using external services. The solution to that is Ingress.


## Ingress

Ingress is the point in the architecture of k8s where all the traffic to a pod enters before being forwarded to the service of that pod.


## ConfigMap

Generally, the endpoints of a pod to which we would be sending requests are configured using the application running within the pod itself. For example, a pod runs a MongoDB database that would have certain configurations of endpoints associated with it. However, any change that we may want to make to the configurations would make us commit and push the changes to version control, build and run the image again in the pod. <br />
This process is simplified by the use of ConfigMaps. They are basically external configurations to our applications. It contains configurational data like the URLs of the databases, etc. After configuring a ConfigMap, we just connect it to a pod so that all changes can get associated to it.


## Secrets

At times, certain external configurations are private (such as credentials to a database that should not go out). We use Secrets instead of ConfigMaps here. All secrets are stored in a base64 encoded format rather than plaintext.


## Volumes

Suppose we are running a SQL database in a pod that handles and generates data. If by any chance the pod goes down, that may mean loss of data. We want our data to be persistent, reliable and long-term. To avoid this, we use Volumes. <br />
Volumes are basically storage disks that may be located on the same local machine that is running the Kubernetes node or a remote storage drive. This ensures that the data is always replicated and stored in the disks, wherever it may be. Kubernetes doesn't manage data persistence. This has to be taken care of in this manner.


## Node Replication

When our application is deployed, it might happen that for some reason our application pod dies. In such a case, users would have to face a downtime. To avoid this, we replicate the nodes so that if something like this happens, the other node would still run pods that would be usable to serve the clients.<br />
A service has been said to have a permanent IP address to a pod. In truth, it is a permanent IP address to all the pods that are attained after the system scales out. That means, if there are 10 nodes running and each would run a pod concerned with a Redis cache, there would only be a single service to all the Redis cache pods. This service also acts as a Load Balancer.


## Deployments

- A set of instructions that specifies the number of pods that would run with respect to only one container in any event and is used to configure the deployment.
- In practice, we would never manually go about creating pods and such services. We would try to automate everything.
- As pods are an abstraction over containers, a deployment too is a layer of abstraction over pods.
- We can in practice replicate any kind of pod reunning whatever containers. However, pods running databases or anything that relates to persistent data (anything that is stateful) cannot be replicated using deployment. The reason is that for that to happen, there must be a mechanism of keeping track of the state, which the basic infrastructure, as of now, is unconcerned with. This is dealt with another component - StatefulSet.


## StatefulSet

- This is a component meant specifically to run applications that are stateful like PostgreSQL, MongoDB, ElasticSearch, etc.
- StatefulSet is for stateful app deployment what Deployment component is for steteless app deployments.
- It is worth noting that this process of setting up StatefulSets in Kubernetes is generally tedious. This is the reason why databases and services like that are hosted externally, not in the k8s cluster. Generally, only Deployments are used here.


## Minikube

In an ideal case of Kubernetes usage, we would be required to run multiple master and slave nodes (more workers than masters). However, allocating resources for master and worker nodes on a single machine of lower specs (most likely any regular laptop) would be difficult. So in order to run a Kubernetes workload on a low spec system, we use an open-source tool called Minikube. It is basically used for testing purposes.<br />
The architecture of Minikube is a bit different since there is nothing like different master and worker nodes. There would exist only one node that shall encapsulate both master and worker processes. That node would have a Docker runtime installed on it. It is basically a one-node k8s cluster that runs on VirtualBox in a local machine. The hypervisor can be VirtualBox or anything else.<br />


## kubectl

The command-line tool that lets us interact with the Kubernetes clusters created is `kubectl`. We recall that the API Server of the Master Process in the single node that Minikube creates is the entry point to the entire node, so to speak. It is responsible for delegating every task and looking into every aspect: creation, maintenance, etc. The API Server can be interacted to in many ways: GUIs, CLIs, APIs, etc.<br />
The CLI tool for interacting with the API Server is `kubectl`. And this is the most powerful and standardized way of doing things. This command is not just limited to Minikube. This can be used for all imaginable purposes.


## Running Minikube

We must have a hypervisor installed for this. Examples include Hyperkit, VirtualBox, VMWare, etc. We may also proceed if we have Docker running on our system. Whatever we choose to use, we have to use the Minikube driver for that software to tell Minikube which hypervisor to use. For example, if VirtualBox is being used:
```sh
minikube start --vm-driver=virtualbox
```
If we want to set any driver permanently so that we don't have to mention it everytime:
```sh
minikube config set driver virtualbox
```