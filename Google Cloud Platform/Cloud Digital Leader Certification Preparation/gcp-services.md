# GCP Services

There are multiple services offered by GCP. The ones that are frequently asked by the exam have been mentioned here.


## Compute Services

There are various compute services provided by GCP. The few commonly asked ones are:
- **Compute Engine**: This service lets us provision and deploy shared VMs that are highly scalable. (We can deploy Docker containers to any Compute Engine VM by enabling container mode while creating the VM)

- **Sole-Tenant Nodes**: This service lets us provision completely dedicated VMs. This may help us meet licensing, compliance and management needs by letting us keep the instances physically separated with the dedicated hardware.

- **Bare Metal**: This service is used to run specialised workloads on the cloud with very low latency by letting us provision complete hardware instead of having VMs. This leaves the choice of hypervisors and virtualisation completely to us.

- **App Engine**: Build and deploy apps on a fully-managed and highly scalable platform without needing to manage underlying infrastructure. This is actually good for apps designed using the microservice architecture.
    - It has a bring-your-own language-runtime using custom docker images.
    - Can easily create test, staging, dev and production environments.
    - We can leverage managed SSL/TLS certificates by default and define access rules with App Engine firewall.
    - Has two types of environments: *Flexible* and *Standard*.
    - **Standard**
        - Described as *serverless* compute.
        - Starts in seconds.
        - Runs in a sandbox.
        - Designed to rapidly scale for sudden traffic spikes.
        - Specific language versions are supported. Not custom runtime.
        - Can scale to zero instances.
        - No SSHing.
        - No background processes.
        - No background processes.
        - Pricing based on hours.
    - **Flexible**
        - Runs with a Docker container on a Compute Engine.
        - Starts in minutes.
        - Designed for predictable and consistent traffic.
        - Supports any language or custom runtimes.
        - Must have at least one instance running.
        - Pricing based on vCPUs, memory and disks.
        - SSHing possible.

- **Cloud GPUs**: Add GPUs to the workloads for ML, scientific computing and 3D visualization.

- **Cloud Functions**: Service used to deploy serverless single-purpose function code that primarily are made to respond to certain events. We just need to write code and deploy - no worries about management of underlying hardware.

- **Eventarc**: To build event-driven solutions by asynchronously delivering events from SaaS, GCP as well as your own apps.

- **VMWare Engine**: Service to migrate and run VMWare workloads natively on GCP.

- **Migrate for Compute Engine**: Migrate servers and VMs from other CSPs or on-premises.

- **Shielded VMs**: Deploy secure and hardened VMs on GCP.

- **Preemptible VMs**: Deploy cheaper, short-lived compute instances suitable for batch jobs and fault-tolerant loads.


## Container Services

It is a specialized form of compute services by GCP that involves the use of containers and clusters.
- **Google Kubernetes Engine**: Efficiently and securely deploy and scale self-containerized Kubernetes apps. Kubernetes was created originally by Google and is now maintained by CNCF.
    - It has the ability to run containers across multiple VMs. This is something that Docker alone cannot do.
    - Pods are a unique component of Kubernetes that represent one or more containers with shared storage, network resources and other shared settings.

- **Cloud Build**: Continuously build, test and run containers using GCP infrastructure.

- **Artifact Registry**: Store, manage and secure container images & language packages.

- **Container Registry**: Store, manage and secure Docker container images. It sounds similar to Artifact Registry because that is Container Registry's successor. It is always recommended to go for Artifact Registry.

- **Cloud Run**: Stateless containers can be run on a fully managed environment or on Anthos.

- **KNative**: Service to deploy and manage serverless cloud-native applications for Kubernetes.


## Platform Services

These services exist to make accessing GCP possible (from any media). We also have a mobile app to monitor GCP but that shall not not be a part of this discussion. Primarily, 4 services exist (that may seem similar but are actually different). They are:
- **Cloud Console**: It is a web-based GUI that runs on the browser and represents the Cloud environment on screen graphically. This is also the simplest (at times more time-consuming way) of utilizing Cloud.

- **Cloud SDKs**: A collection of installable software development tools in one installable package. This can be used to programmatically create, modify, delete or interact with Google Cloud resources.

- **Cloud CLI**: A command line interface processes commands in the CLoud environment in form of lines of text. This is **not** the Cloud Shell. This is meant to be configured into the machine that is interacting with the Cloud. So the use of browsers is not needed here. If GCP resources are to be managed by someone on their machine rather than logging into the browser, this is the way to go.

- **Cloud Shell**: Similar to the CLI, except this terminal is actually built into the online platform. This is the most common medium of accessing cloud resources. And it is faster than the Console. This environment has a BASH shell as well as an online code editor. his is usually the quicker and more general way of doing things in the Cloud.

- **Cloud Code**: Extend your IDE to write, debug and deploy Kubernetes applications for Cloud.

- **Cloud Source Repositories**: Manage code and extend your Git workflows by connecting to all GCP services. Basically a GitHub for GCP that is required to be private.

- **Cloud Scheduler**: Schedule cron jobs, big data jobs and cloud infrastructure operations using a fully-managed cron job service.


## Database Services

Database services are very important among the four-core services that a CSP offers. For GCP, we have:
- **Cloud SQL**: A fully managed RDBMS that is NOT proprietary and supports all known SQL database vendors. We can opt for Cloud Spanner if we want more scalability.

- **BigQuery**: It is a *serverless* (it can scale to zero without any data loss, which is unique for data warehouses since they are expensive and always need to be kept running) data warehouse that stores petabytes of data using a NoSQL wide-column database service. It has built-in ML support as well.

- **Cloud Spanner**: It is a fully managed proprietary (which means that it isn't PostgreSQL or MySQL, etc. It is brand new) RDBMS designed for scale. 

- **Cloud Bigtable**: A NoSQL key-value store database for huge analytic and operational workloads.

- **Firestore**: It is a NoSQL document database (like MongoDB) that is well suited for mobile and web apps. One key feature of it is that *it stores and syncs data in realtime*.

- **Memorystore**: It is an extremely fast in-memory data store similar to Redis.

- **Database Migration Service**: Serverless, easy, minimal downtime migrations to Clould SQL. To migrate open-source relational databases only.


## Data Analytics Services

Data analytics is one major area where GCP shines. The services can seem to be extremely confusing because the only different that there is seems to be the softwares that they use. They are:
- **BigQuery**

- **Google Data Studio**: Service to represent data graphically in form of a story to support better business decisions.

- **Cloud Data Fusion**: Fully-managed service to build and manage data pipelines with no-code integrations and a GUI.
    - It has a drag-and-drop interface. Completely no-code.
    - 150+ preconfigured connectors and transformation.
    - Can be used by a wide variety of audience. Does not require personnel trained for data analysis.
    - Highest price-point.

- **Cloud Life Sciences**: Process, analyse and annotate genomics and biomedical data using containerized workflows.

- **Data Catalog**: Discover and understand data and annotate them and generate metadata using this fully-functional and scalable dtaa discovery service.

- **Pub/Sub**: Ingest event streams of data from anywhere, at any scale. They need to be triggered by certain events.

_ **Cloud Composer**: Create, schedule, monitor and manage data analysis workflows with this fully-managed orchestration service built on *Apache Airflow*.

- **Dataflow**: Develop real-time batch processing and data streaming pipelines built atop *Apache Beam*.
    - It is fully-managed, unlike Dataproc. So less management overhead.
    - Least amount of headaches. Can be used to do things faster.

- **Dataproc**: Develop real-time batch processing, querying and data streaming pipelines built atop *Apache Spark* and *Hadoop*.
    - Apache Spark is known to be the fastest ELT tools. It is around 50 to 100 times fast than other standard ETLs. So that puts it ahead of the other services.
    - The downside is that some management is needed to maintain the pipelines.
    - This supports open-source pipelines (and hence is not fully-managed).
    - Use this for best performance.

- **Dataprep (by Trifacta)**: Explore, clean and prepare datasets for analysis.


## AI & ML Services

Data might need to be fed into pipelines for deriving actual predictive benefits out of them. These services here help us to make use of the data analysed using previous services (or for use in MLOps).
- **Vertex AI**: The fully-managed one stop solution to most AI/ML needs. This is done with the help of Jupyter notebooks and optimised machines with GPU support are used to run such workloads. Amalgamation of AI Platform and Auto ML.

- **AI Platform**: This is the deprecated version of Vertex AI. This service should not be focussed on. 

- **Auto ML**: An automated service that takes in input data and runs automatic algorithms for training models. It is a no-code offering that doesn't need too much of user intervention.

- **Tensorflow Enterprise**: Accelarate and scale ML workflows on the cloud with compatibility tested & optimized *with enterprise quality support*.

- **Vision AI**: Derive insights from text, images, etc. using custom or pertrained models.

- **Video AI**: Enable powerful content discovery and engaging video experiences.

- **Recommendations AI**: Provide a catalog of records that makes recommendations and suggestions to users.

- **Talent Solution**: Capability to create, read, update and delete job postings.

- **NLP API**: An API for NLP.

- **Translation**: Dynamically translate between languages.

- **Document AI**: Use NLP to train and simulate human review of documents.

- **Agent Assist**: Empower human agents by providing continuous support during calls by identifying intent and providing realtime assistance.

- **Dialogflow**: Build engaging voice and text-based conversational interfaces. The 'ES' variant provides a standard agent type for small and simple uses. The 'CX' variant is suitable for very complex and large agents.

- **Text-to-Speech** & **Speech-to-Text** *(self explanatory)*


## Storage Services

- **Cloud Storage**: It is a *serverless* object data store with global edge caching. We only have to pay on the basis of storage and downloads. The available storage classes are:
    - *Standard Storage*: Frequent access of files.
    - *Nearline Storage*: Better option if files need to be accessed only once per month. Cheap.
    - *Coldline Storage*: At-rest access cost is substantially lower but access cost in general is higher than Nearline. Cheaper.
    - *Acrhive Storage*: Ideally for archives that are never meant to be accessed (a sort of an insurance of data). Very slow. 0% SLA. Cheapest.

- **Persistent Disk**: It is a disk drive offering to add the block storage component to VM instances.

- **Cloud Storage for Firebase**: Add Google-scale object storage to your apps using Firebase.

- **Filestore**: To create fully managed, high-performance NFS file servers on Google Cloud. Basically, Persistent Disk is a service that allows only one VM to access it at a time. Filestore is the option that should be chosen for the same use-case, except that it can share to multiple VMs at the same time.


## Networking Services

This is another primary component of the four-core services. They are:
- **Virtual Private Cloud (VPC)**: Logically isolated section of GCP network where (and into whose networks) the other resources can be launched. A range of IP addresses to be designated to the VMs can be chosen using the CIDR range (for example: 10.0.0.0/16 gives 65536 addresses).
    - A subnet is a logical partition of an IP network into multiple smaller network segments. You are breaking up your IP range for VPCs into smaller networks. Subnets have a smaller CIDR range than the main network. The public subnet can reach the internet and the private subnet cannot.
    - **Private Google Cloud** allows the instances to reach Google APIs and services using an internal IP rather than the public IP address. This might be used in conjunction to Cloud NAT (comes later). Using this doesn't by default mean that we have switched to a private subnet.
    - **Shared VPC** shares subnets with other project and connects resources from multiple projects to a common VPC.
    - **VPC Network Peering** privately connects two VPC networks which reduces latency, costs while increasing security. This might seem a bit confusing with Shared VPC but that is particular to networks being shared at a project level.
    - **Serverless VPC Access** allows Cloud Functions, App Engine and Cloud Run services to access resources in a VPC network using their private IPs.

- **Cloud Load Balancing**: This service provides a load balancer to distribute loads and route loads to healthy servers in case some instance is down for some reason. This service is used for traffic distribution.

- **Traffic Director**: Deploy global load balancing across clusters and configure sophesticated traffic control policies for open service mesh.

- **Cloud Router**: Dynamically exchange routes between your Google Cloud Virtual Private Cloud (VPC) network and youron-premises networks using Border Gateway Protocol (BGP).

- **Cloud Interconnect**: To connect your infrastructure to GCP on your terms from anywhere. This provides low latency and high throughput as this service needs an intermediate datacenter to route data to GCP from the native infrastructure. There are two types:
    - **Partnered Interconnect**: A third-party middleman assists in the transfer of data. This is ideal if the organization in question has the capital but doesn't have reserved data centers that they own.
    - **Dedicated Interconnect**: A direct physical connection between Google's network and the on-premises infrastructure. This requires owned data centers. Hosts are high in both cases.

- **Cloud VPN**: Securely extend your on-premises network to Google's network through an IPsec tunnel. The costs are low as compared to the Interconnect option and latency is high as well. No physical connections are required.

- **Cloud CDN**: This service caches the content close to the users using Google's global network.

- **Cloud NAT**: This service provisions instances without public (external) IP addresses while still allowing them to access the internet.

- **Cloud DNS**: Publish and manage domain names using Google's reliable, resilient and low-latency DNS-serving.


## Internal Services

There exist certain services that we *cannot* use. These exist to be used by GCP internally. They may show up as distracting choices in the exam. So these wouldn't generally be the answer.
- **Borg**: A cluster manager running hundreds of thousands of jobs from various different applications across a number of clusters with up to tens of thousands of machines.

- **Collossus**: Cluster-level file system, successor to the Google File System. Provides the underlying architecture of GCP storage and database services.

- **Chubby**: A distributed lock manager as a service that temporarily prevents files and records from being used by another instance.


## Management Services

These services tie in closely with security services as well since both are responsible for management of the resources in the platform. Some services that stand out in terms of overall management:
- **Apigee API Platform**: Used primarily for management of APIs, to provide security policies for identity verification, access control and authentication. Whenever security and APIs are clubbed together, Apigee is most likely to be the answer.
    - It is expensive but has many advanced features.
    - Develop, secure, deploy and monitor APIs from everywhere (inside or outside of GCP).
    - **API Analytics** provide insight into operational and business metrics.
    - **API Monetization**: Easy-to-use solution to realise value from the API.
    - **Apigee Sense**: Protect APIs from attack by adding intelligent behavior detection.
    - **Apigee Hybrid**: Manage APIs on premises or in a hybrid environment.
    - **Cloud Healthcare API**: Help secure APIs that power actionable healthcare insights.

- **Cloud Endpoints**: It is an API Gateway like Apigee but it is much cheaper. It is cheap, simple with good integrations with App Engine.
    - Can be used to develop, deploy and manage APIs on GCP.
    - It cannot be used for security purposes like Apigee.
    - It has a **Developer Portal** that spins up an environment to explore and interact with the API using a GUI in the browser itself, making development much more streamlines and enjoyable.


## Operations Services

This suite of services allows us to monitor, log, debug and troubleshoot apps and services.
- **Cloud Monitoring**: Provides visibility into the performance, availability and overall health of cloud-powered apps.

- **Cloud Profiler**: Continuously gather performance info using a low-overhead CPU.

- **Cloud Logging**: Store, search, monitor and alert on log data and events of GCP and AWS.

- **Cloud Debugger**: Investigate code behaviour in production.

- **Cloud Trace**: Find performance bottlenecks in production.

- **Error Reporting**: Useful for reporting and alerting any type of error that can be custom or predefined via a suitable medium.


## IoT Services

IoTs are physical objects embedded with sensors, softwares and other tech that stream data to cloud services or other edge services.
- **IoT Core**: Securely connect and manage IoT devices using a fully-managed service.


## Media & Gaming Services

Not too frequently asked (like IoT services).
- **Game Servers**: Deliver seamless multiplayer gaming experience to a global player base. Runs on Agones (open-source game server management project running on K8s).

- **OpenCue**: Manage complex media rendering tasks using an open-source render manager.

- **Transcoder API**: Convert video files and package them for optimized delivery to web, mobile and connected TVs.


## Migration Services

Services that can be used to migrate data from on-premises or any other CSPs:
- **Migrate for Compute Engine**: To migrate VMs. The process is:
    - Continuously replicate data from source to target VMs.
    - No source downtime.
    - Quickly clone and test a migrated VM test clones.
    - GCP Console is enough for the entire process.

- **Migrate for Anthos**: To migrate into GKE's containers. We can utilise GKE, Anthos clusters on VMWare and AWS as well. Features are:
    - No charges to use Anthos is required. Subscription is also not needed. Charges for all other services like GKE do apply.
    - Auto-generated container artifacts are used.

- **Cloud Storage Transfer Service**: To migrate storage data of regular volumes. It can be done from another CSP or onlone or from one bucket to another. We can also use it to periodically move data as part of a data prpcessing pipeline.
    - They should be used only when *data size is greater than or equal to 10 TB* and *transfer of data otherwise would take more than a week*.
    - These are actual hardware applicances given by Google. One is 100 TB and another is the 480TB variant.
    - Some features:
        - All SSD drives with fast I/O. Network connectivity options of 10 or 40 GB/s.
        - Ships quickly to and from the Google datacenters.
        - AES 256 encryptions.
        - Safe in transit as well - has customer-managed encryption keys.
        - Tamper and damage resistant external case.

- **Transfer Appliance**: To migrate storage data of large volumes (in TBs or something) and speed is a requirement. Physical drives need to be shipped in this way.

- **Database Migration Service** *(check above)*

- **BigQuery Data Transfer Service**: Automate scheduled data movement into BigQuery using a fully-managed data import service.


## Security Services

This section is extremely important because a lot of questions tend to rise from here.
- **IAM**: Fine-grained identity and access management for resources.

- **Cloud Identity**: Easily manage user identities, devices and applications from one specialised console. It can be understood as a sigle glass pane that allows us to create special accounts just for GCP. This means to use GCP, it is not mandatory to use Google Workspace accounts only (thanks to this service). We can, on top of this service, use IAM to delegate access to these accounts as well. It comes in two versions:
    - **Free**
        - Basic passcode enforcement
        - Basic mobile management
        - Remote account wipe
        - Secure LDAP
        - Google Admin App
        - *Google Cloud Directory Sync* (remember)
    - **Premium**
        - Advanced passcode enforcement
        - Advanced mobile management
        - Security policies
        - Application management
        - App auditing.
        - Reporting


- **Cloud Armor**: A DDoS is a malicious attempt to disrupt normal traffic by flooding a website with large amount of fake traffic. Cloud Armour protects against DDoS attacks as well as provides Web Application Firewall. It has 2 tiers: standard Pay-As-You-Go model as well as Managed Protection Plus starting at $3000 per month. The features that it offers:
    - Detect and mitigate attacks against Cloud Load Balancing workloads.
    - Pre-defined WAF rules to mitigate OWASP Top 10 risks.
    - Named IP lists.
    - Support for multi-cloud or hybrid cloud workloads.
    - Monitoring and visibility.

- **Identity Platform**: Add Google-grade identity and access management to apps. Identity Providers are system entities that create and maintain user identity for a particular platform. A trusted provider of your user identity that lets you authenticate to other services. Identity providers could be Facebook, LinkedIn, Twitter, GitHub, etc.
    - **OpenID**: An identity provider that is more concerned with *who you are*. It is decentralized and open standard. An example is to be able to log into different social media accounts using just a Google account.
    - **OAuth2.0**: An industry standard identity provider that is more concerned with *granting access to functionality*.
    - **Security Assertion Markup Language**: SAML is an open standard identity provider that is useful for single sign-on via web browsers.

- **BeyondCorp Enterprise**: A zero-trust (trust nobody and verify everything) solution that enables secure access with integrated threat and data protection. It enables secure work from virtually any location without the need for a traditional VPN. The features it provides:
    - Single sign-on.
    - Access control policies.
    - Authorization.
    - *User & device based authentication*. <br />
Principles on which it is based:
    - Access to services must not be determined by the network to which a connection is made.
    - Access to services is granted on the user and their devices.
    - Access must be *authenticated*, *authorized* and *encrypted*. <br />
How it actually works is that it encapsulates *user trust* and *device trust* and passes it on to a Global Frontend (in form of context, location and time). The Rules Engine aggregates that data and passes it to the Enforcement Point, which validates the access and allows the user to access the resources. Now, the centers of interest that have been named are actually:
    - User Trust: **Cloud Identity**
    - Device Trust: **Endpoint Verification**
    - Rules Engine: **Access Context Manager**
    - Enforcement Point: **Cloud IAP**, **Cloud IAM**, **VPC Service Controls**.

- **Access Context Manager**: Allows GCP Admins to define fine-grained, attribute-based access control (like device type, OS, IP address, location of accessing) for projects and resources in GCP.

- **Identity Aware Proxy**: (in conjunction with BeyondCorp) Use identity and context to guard access to your apps and VMs. Basically acts as a switch for any resource or service that is hosted. If it is turned on, we can access that resource. If no, we cannot. 'We' in this context might mean the public, the team members, the Admins, etc.

- **Managed Service for Microsoft Active Directory**: Highly available hardened service running Microsoft Active Directory.

- **Security Key Enforcement**: Enforce the use of security keys to help prevent account takeovers.

- **Cloud Audit Logs**: Gain visibility into who did what, when and where for all user activity via logs in GCP.

- **Cloud Data Loss Prevention**: Discover and redact sensitive data. We can detect and protcet sensitive information (*Personally Identifiable Info* and *Protected Health Info*) within GCP storage repositories. The features are:
    - Over 120+ personal information types that it can recognise.
    - Tools to mask, classify, tokenize and transform sensitive data.
    - Create audit reports and dashboards.
    - Schedule inspection jobs directly in the console.

- **Security Command Center**: Centralised security and risk management platform for GCP resources. There is a lot of things that can be done through this platform in terms of security. If the exam asks for the most complete platform to manage security all-in-one, this is the answer. Some important ones:
    - Asset discovery & inventory
    - Threat detection & prevention.

- **Google Cloud directory Sync**: This is used to sync data from Azure AD or LDAP service to the Managed Service of Azure on GCP.

- **Compliance Reports Manager**: It provides users with easy, on-demand access to critical compliance resources at no additional cost. These are just downloadable PDFs actually that show that GCP has the certificate for everything and is compliant with certain terms and conditions. It is just a place to know if GCP follows compliants and be sure of it.