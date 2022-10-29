# Introducing GCP

## Google's Digital Transformation Concept

Digital Transformation is the adoption of newer digital tech to transform business solutions by going paperless and replacing outdated tech with the new. The **Google's Digital Transformation Concept** or the **Google's 7 Solutions Pillar** is:
- **Infrastructure Modernization**: Replacing legacy hardware and software systems with cloud solutions. Hybrid infrastructure and infrastructure mobility chosing a mix of best CSPs for their organization. Ex: *Anthos*.
- **Application Modernization**: Building apps on the Cloud allows the delivery to be much faster and convenient. It gives us excellent automations and pipelines, ability to rollback changes done in production as well as gives us a testing ground. Ex: *App Engine*.
- **Smart Analytics**: Data can be stored on Cloud to perform certain operations on it for gathering analytics and business intelligence. Ex: *Looker*.
- **AI**: Prior to the adoption of Cloud, AI and ML were domains that required specialised personnel to support study and research. Modern innovations, however, has made it easier for AI to be incorporated. Ex: *Vertex AI*. 
- **Security**: Security is always being upgraded and taken care of in the Cloud. Latest and the most recognised technologies are being used to secure all resources and data in Cloud.Ex: *IAM*.
- **Business Applications platform portfolio**: The CSPs are built atopn robust and well-documented APIs that are standardized. So, business solutions can focus on building themselves up and the use the APIs provided by the CSPs rather than having to reinvent the wheel. Ex: *Cloud SDKs*, *GCP API Docs*, etc.
- **Database and storage solutions**: CSPs have guaranteed SLAs of data durability as well as migrate and secure data. Ex: *Cloud Storage*.


## Shared responsibility Model

The Shared responsibility Model (SRM) is a simple visualisation that helps in determining what the customer is responsible for and what Google is responsible for within the GCP platform. For every type (IaaS, PaaS, SaaS) of cloud computing in GCP, we have different levels of responsibilities. The responsibilities that *we* have are:
1. **SaaS**: Content, access policies, usage.
1. **PaaS**: Content, access policies, usage, deployment, web app security.
1. **IaaS**: Content, access policies, usage, deployment, web app security, access and authentication, identity, operations, network security, guest OS.<br />
The basic rule of thumb is - *"if you've configured it, you're responsible for it"*.


## Understanding SRM for Compute Services

There are many compute services. Some are categorised as IaaS, some PaaS, etc. Here we compare the SRM for the Compute Services:
1. **IaaS**:
    - **Bare Metal**: Gives us bare metal access to a machine. This leaves a lot of configurations such as host OS, hypervisors to us. *Google is only responsible for the physical machine.*
    - **Sole-Tenant Node**: A VM that is provisioned solely and completely for us. We do not have to share it with anyone else, which is unlike the case of a Compute Engine.
    - **Virtual Machine**: Gives us a VM. We have to figure out the container runtimes and the host OS configurations. *Google is responsible for the hypervisor and the physical machine.*
    - **GKE**: This service is used to manage clusters and containers. We have to configure, deploy and manage storage of containers. *Google is responsible for hypervisor, the OS and the physical machine.*
1. **PaaS**:
    - **App Engine**: Used to create and deploy apps easily without appreciable manual efforts. Google takes care of a lot of things and a lot of things are handled by them. We just need to upload the code, set up some basic configurations, put the environment variables (if needed) in place and deploy with a selected strategy.
1. **SaaS**: For most SaaS products (in the Workspace), we have to manage just the contents and access controls. The rest is handled entirely by Google.
1, **FaaS**: Services like *Cloud Run* and *Cloud Functions* are serverless and almost everything is done by Google itself. We just need to upload the code.


## The Google Cloud Network

- The Google Cloud Network is a network that has been designed to be centres of operations with respect to its Cloud services. There are 5 major regions as yet: North and South America, Europe, Asia and Australia.
- The choice of a node network location affects: latency, availability and durability.
- A location is divided into Regions and Zones.
- Regions are independent geographic areas that consist of zones. They generally have 3 zones (exceptions have been noticed).
- A Zone is a subdivision of a Region that has Google datacenters and resources to be the nodes.
- For example, a VM running within a Region may switch Zones if something goes wrong in the chosen zone. This is called **Zone Redundancy**.
- Some services allow us to have **Region Redundancy** as well (like *Cloud Storage*). If a complete region, due to some natural disaster, goes down, we can switch over to the other region.
- Approximately, 88 Zones and 29 Regions are supported.
- It is a common practice to have three zones just to ensure high availibility, even if something goes down.
- To meet the compliance boundaries, we need to enable the feature of *Assured Workloads* that allows us to apply various security controls to an environment. It includes data residency, among a whole lot of other things.


## Resource Scoping

Products and services all have their scopes that are based on:
1. **Zonal Resource**: Resources residing in a zone within one region.
1. **Regional Resource**: Resources residing in multiple zones within one region.
1. **Multi-Regional Resource**: Resources residing in specific zones within multiple regions.
1. **Global Resource**: Resources reside globally.<br />
There are Internal Services as well that we do not deal with directly. They are managed and operated on by Google and we are indirectly related to them.


## Cloud Interconnect

This is a GCP Service that provides direct physical connections between the on-premises network and Google's network. Large amounts of data can be transferrede between networks. This can be more cost-effective than buying additional bandwidth over the public internet.<br />
There are two offerings:
- **Dedicated**: A direct connection between the on-premises network and the Google's network via a *co-location facility* (it is a data-centre where space, equipment and bandwidth are available for customers who want to rent). Between 10 Gbps - 200 Gbps. 
- **Partner**: A direct connection between the on-premises network and the Google's network via a *trusted third-party*. Between 50 Mbps - 10 Gbps. <br />
At times being able to rent a dedicated medium is extremely difficult and organisations may have to settle for third-parties. Cost can also be a factor sometime.


## GCP for Government

The public sector involves public goods and governmental services such as militay, law enforcement, healthcare, transit, etc. GCP can be utilised by the public sector or organisations developing cloud workloads for the public sector. GCP achieves this by meeting regulatory compliance programs along with specific governance and security controls. Some programmes are:
1. **FedRAMP**: A US government-wise programme that provides a standardized approach to security assessment, authorization and continuous monitoring for cloud products and services. Any CSPs would provide for an isolated region just to run FedRAMP workloads. These are called **GovClouds**. Due to the isolation, offerings might seem degraded, availibility might seem low and operation cost might seem high. GCP has an alternate offering to **GovCloud** where the workloads run in the usual GCP datacenters. This eliminates all the cons of using a **GovCloud**.


## Evolution of Computing Power

Computing Power is the throughput measured at which the computer can complete a computational task. For GCP, the service offerings can be categorized as:
1. *Compute Engine* for general computing.
1. *Cloud TPU* for tensor computing. Here, the Tensor Processing Unit is 50x faster than the traditional CPU.
1. *Google Quantum AI* for quantum computing. It has the capacity to be million times faster. Google has produced several hardware for such things (even if the whole concept is in its infancy). The products include Foxtail, Bristlecone and Sycamore.


## Folders & Projects

- A **Project** in GCP s a logical grouping of resources. Every cloud resource must belong to a project. A project can't access the resources of another project unless *VPC Network Peering* or *Shared VPC* is being used.
    - Every project is made up of settings, permissions and other metadata.
    - Resources within a single project can easily work together.
    - Every project has a name (we choose), an ID (either us or GCP can choose; unique across GCP) and a project number (GCP chooses). These identifiers are important as they can be used in certain API calls.
    - A project can be deleted but its ID can never be used again.
    - A project may serve as a namespace, which means that resource names may be reused across different projects but should be unique within a single project.
    - When billing is enabled, each project is associated with a billing account. Multiple projects can have their resource usage billed to the same account, though.
- A **Folder** allows the logical grouping of multiple projects that share IAM permissions. They are used commonly to isolate projects for different departments or for different environments. For example, we may have a project for the beta version of an app and another for the regular version. We may have two different folders for this type of thing - one for development and one for production, each of which should have these 2 projects for proper streamlined workflow.