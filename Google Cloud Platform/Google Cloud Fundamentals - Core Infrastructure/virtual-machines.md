# Virtual Machines

A VM is a basic unit that acts as an instance. The systems in the datacenters are all hypervised and they are made to be segregated into VMs with different hardware specifications that suited specific types of applications for all the services. If we are to create a very general type of a VM for a general purpose that doesn't cater to something too specific (for example: having an instance to host a backend API for a website, a Jenkins or Nginx server instance, etc.), we choose the *Compute* services.


## Virtual Private Cloud

Google Cloud Virtual Private Cloud (VPC) provides networking functionality to Compute Engine virtual machine (VM) instances, Kubernetes Engine containers, and App Engine flexible environment. In other words, without a VPC network you cannot create VM instances, containers, or App Engine applications. Therefore, each Google Cloud project has a default network to get you started.<br />
You can think of a VPC network as similar to a physical network, except that it is virtualized within Google Cloud. A VPC network is a global resource that consists of a list of regional virtual subnetworks (subnets) in data centers, all connected by a global wide area network (WAN). VPC networks are logically isolated from each other in Google Cloud.
- It is a secure, virtual, individual and private cloud-computing model hosted within a public cloud. This private cloud is hostel remotely by the cloud provider.
- VPC networks connect Services & resources to each other. Networks are segmented and **firewall rules** are used to restrict network access to instances. Traffic can be forwarded to specific destinations using **static routes**.
- VPC networks are global and can have subnets in any Google Cloud region worldwide.
- Consider a VPC network having one network with one subnet defined in GCP's us-east1 region. If we have 2 VM instances in that subnet, they can belong to different zones within that same subnet.
- This capability can be used to build solutions resilient to disruptions yet maintain a simple network layout.


## VPC Compatibilities

- Like most physical networks, **Routing Tables** are here as well. Their utility is to forward traffic from one instance to the other within the same network, different subnetworks or even different zones. External IP addresses aren't needed. We don't need to provision the tables and they are built-in.
- A globally distributed **Firewall** is provided by the VPC that we don't have to configure or put together. That is a solution that lets us restrict access to the instance from certain kinds of traffic. We may use tags onto instances to specify which **firewall rule** applies to which instance.


## Compute Engine

- This is Google's IaaS solution that lets us run VMs on the infrastructure.
- Each Compute Engine (VM) has the power to operate like its own physical server because of its funcationality and power that resembles an OS completely.
- There is no upfront investment involved.
- The Shell or the Console may be used to create these resources. They can be reconfigured with respect to the hardware as well as the OS images (we can get customised images or choose from the ones that Google provides). 
- The *Marketplace* is a good place to get started as it offers preconfigured and readymade solutions pertaining to certain use-cases. We can easily choose a template of an instance to get started and, if required, make some modifications on our own to it as well. There is no extra charge involved for the use of *Marketplace* instances. Some may charge extra just because it comes bundled up with some thrid-party software package. The estimate breakdown will show such charges.
- **Billing**: It bills the users by the second (minimum one minute). Charges are calculated on a monthly basis. If the instance runs for 25% of the month, **sustained-use discounts** are recieved on the total bill by the minute. **Committed-use discounts** can also be applied (upto around 57%) if a committed workload runs on the VM everytime (based on vCPU and memory metrics). We need to commit to use that for a term of upto 1 or 3 years.


## Scaling Virtual Machines

- The *Compute Engine* has a feature called **Autoscaling** that allows the addition or removal of more VMs when the usage exceeds the capabilities of the VM (based on Metrics). **Scaling Out** is favoured over **Scaling Up** by new customers and users since using a large *Compute* resource would require certain attention from the users or some specialized skill.
- VPC supports many types of **Load Balancing** as well.


## Load Balancing

- **Autoscaling** is the process by which an instance, upon having its resources exhausted, brings into its cluster another VM or migrates to another VM of increased capacity (depending upon the mode of autoscaling).
- **Load Balancing** is the process of directing traffic to all the instances that might be present, at any given time, in a given architecture. A web app may have 2 or 100 instances at the same time, depending upon the traffic that it recieves. Whatever might be the case, there should exist proper ways to route and spread the traffic to all the instances.
- It is a fully managed and predefined service that can be put in front of all sorts of incoming traffic to spread them out.
- VPCs offer a suite of options:
  - Cross-regional Global HTTP(s) Load Balancing for web applications.
  - For Secure Sockets Layer traffic not HTTP, use Global SSL Proxy Load Balancing.
  - For other TCP connections that don't use SSL, use a Global TCP Proxy Load Balancing.
  - To handle UDP traffic, we use Regional Load Balancer.
  - To distribute traffic from within the application itself, use Regional Internal Load Balancing.


## Google Domain Name Service (DNS)

- *Google 8.8.8.8* is the public DNS provided by Google. A DNS is what translates the hostnames into addresses over the internet.
- Google *Cloud DNS* is the service that is used within the GCP infrastructure to be a managed DNS service to run in the same infrastructure that 8.8.8.8 runs on. The applications developed with GCP as the part of the Cloud stack take the advantage of this service to translate hostnames to addresses.
- DNS information is served from redundant locations from all around the world.
- The DNS is also programmable and also uses **edge caching**, which refers to the availibility of cache servers close to the main server for speed.


## Cloud Content Delivery Network (CDN)

- This service can be used to accelerate content delivery in systems. Low network latency will be experienced. Reduced load is observed at the content origins.
- This can be enabled by a single checkbox after setting up Cloud Load Balancing.
- It can also help save money.


## Connecting VPCs to Other Networks

- We can connect the VPCs to other networks as well like on-premises server architectures, etc. There are many ways for this.
- We can use the *IPCSec VPN Protocol* service to make use of the internet to connect the networks to the VPC over a VPN using the Border Gateway Protocol. Not always the best option because of the security issues and bandwidth concerns.
- *Direct Peering* can be an option that would mean to put a router in the same datacenter with a Google Point of Presence (> 100 all over the world). Router is used to exchange traffic.
- *Carrier Peering* is an option that gives one direct access from an on-premises network through a service provider network by exposing public IP addresses of the Cloud services used. It is not something that is covered by the Google Service Agreements so that's a con.
- *Dedicated Interconnect* is a service that is used for one or more direct connections to Google. VPN can also be used.
- *Partner Interconnect* just puts a middleman between the previous architecture. This is also 99.99% SLA secure. Good especially for cases when a datacenter is in a physical location that cannot reach a Interconnect colocation facility by Google.


## Lab: Getting Started With the VPC

- Every project by default has a VPC. Without VPC, the Networking component of any Cloud resource cannot be completed and hence, no services can be used.
- We can create more VPCs by ourselves as well. This can be seen in *VPC Networks*.
- Routes tell VM instances and the VPC network how to send traffic from an instance to a destination, either inside the network or outside Google Cloud. Each VPC network comes with some default routes to route traffic among its subnets and send traffic from eligible instances to the internet. We can create our own as well.
- We can see the **Firewall Rules** as well. They are the protocols that allow the ingress and egress of traffic to our systems through our network. There are four in number by default. These firewall rules allow ICMP, RDP, and SSH ingress traffic from anywhere (0.0.0.0/0) and all TCP, UDP, and ICMP traffic within the network (10.128.0.0/9). We may create our own.
- The `allow-icmp` firewall rule is required to ping an instance using its external IP while the `allow-custom` is used for its internal IP. The `allow-ssh` rule allows an SSH connection to hold, without which SSH is not posssible. 