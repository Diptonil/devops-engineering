# Three Node Swarm Cluster

Our objective here is to run a cluster having three nodes. A node would correspond to a container running singly in a single machine. This means all the containers would be housed in a system separately. For convenience, we may take VMs to mimic a whole system. <br />
The Shell script clearly tells us what commands we need to execute in each node to get the final result.


## Steps

1. Create three VMs to mimic three nodes.
1. We would initialize Swarm on a VM. Initialization would be specialized. We would advertise our public IP address for all nodes to have network accessibility. This would be the *leader* manager node.
1. The command that gets spit out is used on the other machines so that they can join the cluster as *worker nodes*. We could promote our worker nodes to be a manager node by appending a `manager` in the `join` command. But we wouln't do that here.
1. We can handle all managerial functions of the other nodes from the manager node. This includes the power to delegate manager status as well (so we can also use this alternative instead of using join manager).
1. Then we start up in the leader node the service to spin up three replicas of a container (whatever it might be - for simplicity we'll assume the Alpine Ubuntu image).
- We can observe that our nodes are indeed running succesfully.