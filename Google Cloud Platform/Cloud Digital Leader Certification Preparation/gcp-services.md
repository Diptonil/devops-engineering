# GCP Services

There are multiple services offered by GCP. The ones that are frequently asked by the exam have been mentioned here.


## Compute Services

There are various compute services provided by GCP. The few commonly asked ones are:
- **Compute Engine**: This service lets us provision and deploy shared VMs that are highly scalable.

- **Sole-Tenant Nodes**: This service lets us provision completely dedicated VMs. This may help us meet licensing, compliance and management needs by letting us keep the instances physically separated with the dedicated hardware.

- **Bare Metal**: This service is used to run specialised workloads on the cloud with very low latency by letting us provision complete hardware instead of having VMs. This leaves the choice of hypervisors and virtualisation completely to us.

- **App Engine**: Build and deploy apps on a fully-managed and highly scalable platform without needing to manage underlying infrastructure. This is actually good for apps designed using the microservice architecture.
    - It has a bring-your-own language-runtime using custom docker images.
    - Can easily create test, staging, dev and production environments.
    - We can leverage managed SSL/TLS certificates by default and define access rules with App Engine firewall.
    - Has two types of environments: *Flexible* and *Standard*.
    - **Standard**
        - Described as serverless compute.
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

- **VMWare Engine**: Service to migrate and run VMWare workloads natively on GCP.

- **Migrate for Compute Engine**: Migrate servers and VMs from other CSPs or on-premises.

- **Shielded VMs**: Deploy secure and hardened VMs on GCP.

- **Preemptible VMs**: Deploy cheaper, short-lived compute instances suitable for batch jobs and fault-tolerant loads.


## Container Services

It is a specialized form of compute services by GCP that involves the use of containers and clusters.
- **Google Kubernetes Engine**: Efficiently and securely deploy and scale self-containerized Kubernetes apps.
- **Cloud Build**: Continuously build, test and run containers using GCP infrastructure.
- **Artifact Registry**: Store, manage and secure container images & language packages.


## Anthos

Manage compute from both on-premises as well as public cloud in a single unified interface.


## Looker

A data exploration and BI platform currently owned by Google and hence a part of GCP.


## Security Command Center

A centralized security platform for control and visibility.


## BeyondCorp

A zero-trust model security framework.


## Platform Services

These services exist to make accessing GCP possible (from any media). We also have a mobile app to monitor GCP but that shall not not be a part of this discussion. Primarily, 4 services exist (that may seem similar but are actually different). They are:
- **Cloud Console**: It is a web-based GUI that runs on the browser and represents the Cloud environment on screen graphically. This is also the simplest (at times more time-consuming way) of utilizing Cloud.

- **Cloud SDKs**: A collection of installable software development tools in one installable package. This can be used to programmatically create, modify, delete or interact with Google Cloud resources.

- **Cloud CLI**: A command line interface processes commands in the CLoud environment in form of lines of text. This is **not** the Cloud Shell. This is meant to be configured into the machine that is interacting with the Cloud. So the use of browsers is not needed here. If GCP resources are to be managed by someone on their machine rather than logging into the browser, this is the way to go.

- **Cloud Shell**: Similar to the CLI, except this terminal is actually built into the online platform. This is the most common medium of accessing cloud resources. And it is faster than the Console. This environment has a BASH shell as well as an online code editor. his is usually the quicker and more general way of doing things in the Cloud.