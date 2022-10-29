# Cloud Architecture Terminologies

- **Servers** or **Instances** or **Nodes**: Host machines that run workloads.
- **Datacenters**: A secured building having thousands of computers acting as hosts.
- **Dedicated Instances**: A single machine that has been rented or brought for complete use by just a single customer. Replacing or scaling these servers are very difficult. Manual migrations can be time consuming. Capacity needs to be guessed properly otherwise payment has to be made for underutilization. The biggest pro is the guarantee of full security, privacy and utilization of underlying resources.
- **VM Instances**: Many VMs run on a single machine. Hypervisor is the software layer that makes it possible for the VMs to be run on the system concurrently. It is shared by multiple customers. Scaling and migrating is far more simpler. However, it isn't suited for running multiple workloads on the same VM Instance, since it may lead to conflicts during resource sharing.
- **Container Instances**: They are just instances running within a VM instance. This is achieved with the help of a Docker Daemon. Very cost-effective. Resource utilization is maintained well. Very useful for running multiple apps in the same environment with no resource tug-of-war. This makes it useful to run microservices.
- **Serverless Computing**: This process utilizes servers (of course), but is named so because we *do not need to care about any servers*. We can just upload the code, choose duration up till when the instance should run and the memory to allot for running the code. The CSP takes care of the rest.
- **Cold Starts**: When an instance takes a longer time to start up (for whatever reason), certain operations that it is expected to be able to execute might get skipped out on. This is called a cold start.
- **Healthy Servers**: Machines that are in the oeprational state. Unhealthy machines are the ones that either face hardware difficulties, power outages, excessive loads, et cetera that basically impede the workloads from functioning.


- **Latency**: Time delay between two physical systems. For inter-regional latencies, it is generally triple digit (around 500 ms) and for inter-zonal latencies, it is double digit (around 10 ms). The numbers would vary, of course. 
- **Lags**: Noticable time delay between the input actions and the reactions of the server sent back.
- **Availibility**: Ability to ensure that the service remians available and accessible throughout.
- **Scalability**: Ability to grow rapidly.
- **Scaling Up** or **Vertical Scaling**: Upgrading to a bigger machine to handle increasing workloads.
- **Scaling Out** or **Horizontal Scaling**: Increasing the number of similar machines to handle increasing workloads.
- **Elasticity**: Ability to grow *or shrink* rapidly.
- **Fault Tolerance**: Ability to prevent a failure.
- **Disaster Recovery** or **Durability**: Ability to recover from a failure *without the loss of data*.
- **Single Point of Failure**: Situation of having only one server source to handle entire workloads which, for some reason, fails, causing the entire system to go down.
- **Redundancy**: Avoiding single point of failures by maintaining servers that can act as a backup in case the primary server fails.
- **Fail-Overs**: The situation in which due to any failure, traffic is shifted from the primary server to one or many other redundant servers.
- **Data Residency**: The geographical location of where an organization or cloud resources reside.
- **Compliance Boundaries**: Regulatory compliances by the government or any organisation that describes where and how data and cloud resources are allowed to reside.
- **Load Balancing**: Keeping an intervening machine that has the job to *evenly distribute traffic* and *route traffic to healthy instances*, in case some instance fails.


- **Edge Networking**: Practice of having the servers as close to the clients to deliver the lowest latency and save bandwidth.
- **Points of Presence**: An intermediate location between a GCP Region and the client. It could be a collection or hardware or a datacenter.
- **Edge PoP**: A location where an user can ingress quickly into the GCP network for accelarated access to cloud resources.
- **CDN PoP**: A location to segress cached website, assets, files, et cetera for quicker load-times.
- **Cloud Media Edge**: A location specialised for media delivery.