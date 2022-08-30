# Cloud Computing

It is the way of using Information Technology to achieve the five listed goals:
1. Customers get compute resources that are on-demand.
1. Customers may access those resources from anywhere.
1. Providers of the resources allocated them resources out of their pool.
1. Customers pay only for what they use.
1. Customers can scale up or down their demands.

We can say that Cloud is a network of remote servers that are hosted on the internet to store, manage and process data as well as offer multiple utilities on the web rather than using a personal computer on its own for the same purposes.


## History of Servers

1. **Dedicated Server**: It is a single machine for a single organization. It can run only one application. Very expensive & high maintainance with good security. There still are dedicated servers all around us, although people are slowly gravitating away from it.
1. **Virtual Private Server**: It too is a single machine for a single organization. It is just virtualized into sub-machines. It can run multiple applications due to virtualization into different systems, making effective (and sometimes excessive) use of the resources of that one machine. Virtual Machines introduced first by VMWare had a lot to contribute to this phase.
1. **Shared Hosting**: This got popular in the 2000s by companies like GoDaddy. The philosophy is letting users rent a machine assuming the under-utilization of resources by them. This is extremely cheap and limited. One machine is used by hundreds of users for their purposes. The con is that for a single machine being used, if one person renting the shared hosting overuses the resources, the others suffer.
1. **Cloud Hosting**: This involves multiple machines being used as one system. The system is then abstracted into different services. They're secure, scalable & cost-efficient. The philosophy is that one has to limit to whatever they wish to use & pay for just that. This is the phase where we are at now.


## Types of Services in Cloud

1. **Software as a Service (SaaS)**: These are for customers who consume a particular software. It's a product run and managed by the service provider (Salesforce, Google Workspace Suite, Office 365, etc.). We don't need to worry about anything and can just consume the applications and services without any mandatory operational skills. These applications are not installed on our computer and hence belong to the Cloud.
1. **Platform as a Service (PaaS)**: These are services for developers. It's a platform for deployment of apps managed by the service providers. (Heroku, Beanstalk, Digital Ocean). The developers don't worry about provisioning, configuring or understanding the underlying architecture to utilize the services. It is ideal when a certain degree of autonomy is required in configuring the deployments.
1. **Infrastructure as a Service (IaaS)**: These are services for the administrators or DevOps engineers who specialise in the operation of Cloud technologies. Highly configurable, this level is concerned with having the maximum possible autonomy and freedom in configuring the Cloud services at each minute factor.
1. **Serverless Technologies (FaaS)**: Known as 'Functions as a Service', the focus is mainly on generating code and not at all in any part of the deployment process. The Cloud is expected to take care of it by itself. The *Cloud Run* as well as *Cloud Functions* are two such servuces offered that are serverless. We just write code and deploy it on a server for it to keep on executing.


## The Google Cloud Network

- The Google Cloud Network is a network that has been designed to be centres of operations with respect to its Cloud services. There are 5 major regions as yet: North and South America, Europe, Asia and Australia.
- The choice of a node network location affects: latency, availability and durability.
- A location is divided into Regions and Zones.
- A Region is a place where there are supposed to be server nodes.
- A Zone is a subdivision of a Region that has Google datacenters and resources to be the nodes.
- For example, a VM running within a Region may switch Zones if something goes wrong in the chosen zone. This is called *Zone Redundancy*.
- Some services allow us to have *Region Redundancy* as well (like *Cloud Storage*). If a complete region, due to some natural disaster, goes down, we can switch over to the other region.
- Approximately, 88 Zones and 29 Regions are supported.


## Security Measures

Google implements certain security techniques that are of paramount importance in the proper functioning of multiple services available to the users:
1. The Hardware Infrastructure Layer:
   - Hardware design is done by Google itself to ensure quality and assurance.
   - Secure boot stack is implemented.
   - Physical security to the datacenters is always given importance to.
2. Service Deployment Layer:
   - Inter-service communication encyrption is done to secure Google's communication process with itself for fetching and manipulating data.
3. User Identity Layer:
   - User Identity features go beyond just asking for passwords and emails.
4. Storage Services Layer:
   - Google ensures that hardware encryption support is enabled for data and file storage.
5. Internet Communication Layer:
   - Google Front End ensures all TLS connections are ended using a public-private key-pair.
   - Denial of Services Attacks are prevented from occuring due to the multi-layered architecture supported by Google.
6. Operational Security Layer:
   - Intrusion detection.
   - Reducing insider risk.
   - Software development practices.
   - U2F use.


## Quiz

1. Select two fundamental characteristics of cloud computing from this list.
- [x] Customers can scale their resource use up and down.
- [ ] Customers are required to commit to multi-year contracts.
- [ ] Providers always dedicate physical resources to each customer.
- [ ] All resources are open source.
- [x] Resources are available from anywhere over the network.
1. Which one of the following statements is true regarding the ability to scale cloud computing resources up and down?
- [ ] Cloud computing does not provide a way to scale resources. 
- [ ] Only CPU and memory resources are elastic.
- [ ] Only storage resources are elastic.
- [x] CPU, memory, and storage resources are elastic.
1. What cloud computing service binds application code to libraries that give access to the infrastructure an application needs?
- [x] Platform as a service
- [ ] Infrastructure as a service
- [ ] Virtualized data centers
- [ ] Hybrid cloud
- [ ] Software as a service
1. What cloud computing service provides raw compute, storage, and network resources that are organized similarly to physical data centers?
- [x] Infrastructure as a service
- [ ] Database as a service
- [ ] Software as a service
- [ ] Platform as a service
1. Why might a Google Cloud customer use resources in several zones within a region?
- [x] For improved fault tolerance
- [ ] For expanding services to customers in new areas
- [ ] For better performance
- [ ] For getting discounts on other zones
1. Who benefits the most from billing by the second for cloud resources, such as virtual machines?
- [ ] Customers who create too few virtual machines to get discounts
- [x] Customers who create and run many virtual machines
- [ ] Customers who create virtual machines that run commercially licensed operating systems
- [ ] Customers who create many virtual machines and leave them running for months