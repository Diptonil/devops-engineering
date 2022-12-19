# Virtual Machines

The *Compute Engine* service is purely IaaS. It gives the most flexibility in all respects and can be the most difficult to maintain as well, if not done properly. At its heart, it's just physical servers, running inside the Google Cloud environment, with a number of different configurations. Both predefined and custom machine types allow you to choose how much memory and how much CPU you want. You choose the type of disk you want, whether you want to use persistent disks backed up by standard hard drives or solid-state drives, local SSDs, Cloud Storage, or a mix. You can even configure the networking interfaces and run a combination of Linux and Windows machines.


## Machine Types

- **General Purpose**: Most flexible, the best choice for most cloud operations when the exact task is generalised, the go-to machine for personnel with not extreme knowledge of Cloud can opt for.
    - **E2 instances** are perfectly designed for day-to-day tasks, especially when we don't have any heavy application specific dependency on our machine. It is suitable for serving web and app backends, development environment for general organisational cases, mircoservices, etc. It offers further segregation of resource-offerings. The E2 machine series also contains shared-core machine types that use context-switching to share a physical core between vCPUs for multitasking. Shared-core E2 machine types have 0.25 to 1 vCPUs with 0.5 GB to 8 GB of memory.
    - **N2 and N2D instances** are the next generation following N1 VMs, offering a significant performance jump. N2 and N2D are the most flexible VM types and provide a balance between price and performance across a wide range of VM shapes, including enterprise applications, medium-to-large databases, and many web and app-serving workloads.
    - **Tau T2D VMs** are optimized for cost-effective performance of demanding scale-out workloads. T2D VMs are built on the latest 3rd Gen AMD EPYCTM processors and offer full x86 compatibility. They are suited for scale-out workloads including web servers, containerized microservices, media transcoding, and large-scale Java applications. T2D VMs come in predefined VM shapes, with up to 60 vCPUs per VM and 4 GB of memory per vCPU. If you have containerized workloads, Tau VMs are supported by Google Kubernetes Engine to help optimize price-performance. 
- **Compute Optimized**: Has the highest performance per core on Compute Engine and is optimized for compute-intensive workloads.
    - **C2 VMs** are the best fit VM type for compute-intensive workloads, including AAA gaming, electronic design automation, and high-performance computing across simulations, genomic analysis, or media transcoding. They might also be applications that have very expensive per core licensing and thus would benefit from higher per core performance.
    - **C2D** machine type series provides the largest VM sizes and are best-suited for high-performance computing (HPC). The C2D series also has the largest available last-level cache (LLC) cache per core. The C2D machine series come in different machine types ranging from 2 to 112 vCPUs, and offers 4 GB of memory per vCPU core.
- **Memory Optimized**: The memory-optimized machine family provides the most compute and memory resources of any Compute Engine machine family offering. They are ideal for workloads that require higher memory-to-vCPU ratios than the high-memory machine types in the general-purpose machine family.
    - **M1 machine** series has up to 4 TB of memory, while the M2 machine series has up to 12 TB of memory. These machine series are well-suited for large in-memory databases such as SAP HANA, as well as in-memory data analytics workloads. Both the M1 and M2 machine series offer the lowest cost per GB of memory on Compute Engine, making them a great choice for workloads that utilize higher memory configurations with low compute resource requirements.
- **Accelarator Optimized**: This family is ideal for massively parallelized Compute Unified Device Architecture (CUDA) compute workloads, such as machine learning (ML) and high-performance computing (HPC). This family is the optimal choice for workloads that require GPUs. The A2 series has 12 to 96 vCPUs, and up to 1360 GB of memory. Each A2 machine type has a fixed number (up to 16) of NVIDIA’s Ampere A100 GPUs.


## Custom Machine Type

- If none of the predefined machine types match your needs, you can independently specify the number of vCPUs and the amount of memory for your instance.
- The cost is slightly more for similar specs.
- Only machine types with 1 vCPU or an even number of vCPUs can be created. Memory must be between 0.9 GB and 6.5 GB per vCPU (by default).
- The total memory of the instance must be a multiple of 256 MB.


## OS Images

- We can have both custom and public base images.
- The base prices for the use of these images are global since they don't depend on geography.
- We can import any custom OS image that we have from on-premises or any other cloud vendor.
- We can also have premium images (they're marked as premium). The additional charge after a one-minute-minimum for use of those images have to be incurred.
- Linux images - popular distros - are available such as CentOS, CoreOS, Ubuntu, etc. Windows images of Windows 20xx servers can also be chosen (some are premium). Windows SQL server is also premium with a ten-minute minimum additional charge.


## Storage

- The three options are Standard, SSD or local SSD.
- Local SSDs have even higher throughput and lower latency than SSD persistent disks, because they are attached to the physical hardware. However, the data that you store on local SSDs persists only until you stop or delete the instance. Typically, a local SSD is used as a swap disk, just like you would do if you want to create a ramdisk, but if you need more capacity, you can store those on a local SSD.
- You can create instances with up to eight separate 375-GB local SSD partitions for a total of 3 TB of local SSD space for each instance.
- Standard and non-local SSD disks can be sized up to 257 TB for each instance.


## VM Access

- The way to access a VM that is created is dependent on the OS being used. 
- **Linux**:
    - The instance must allow TCP at port 22.
    - We can SSH directly through the console.
    - We can SSH through the Shell using a command.
    - We can SSH through agents like PuTTY, or even our own systems by generating key-pair.
- **Windows**:
    - The instance must allow TCP at port 3389.
    - We must set up a Windows password first through the Console and then RDP through our systems.


## VM Lifecycle

- **Provisioning**: The instance gets created. Various resources, at the hardware level, are allotted at the datacenters to set up a machine with the requested specifications.
- **Staging**: Software resources are allotted at the base level such as the OS image, network configurations are made and IPs are assigned.
- **Running**: An instance starts up normally. Startup scripts are all executed. Only then can we use SSH/ RDP to access it.
- **Stopping**: Shutdown scripts are executed. Before closing down, resources (dangling ones) are cleared off. A snapshot of the state might be taken.
- **Terminating**: VM is closed off. It may also be deleted in the next step if the user wants. If there is some availibility policy that may resurrect it, it can be restarted, in which case it begins its cycle from the phase of provisioning. <br />
We may also reset a system if need be. Preemptible VMs also have a stage in which they are preempted in their execution. The maintainance policy for a VM, by default, is to live migrate a system so that usage may be continued. But we may choose to terminate such instances instead, if we would want to.


## Stopped VMs

- We cannot change the image of a terminated VM. There are a whole lot of other changes we can make, however.
- We can change machine types on a terminated VM.
- We stop to pay for the machine when it is terminated. However, we **still pay** for the storage that we avail using the persistent disks.


## Sole-Tenant Nodes

- If you have workloads that require physical isolation from other workloads or virtual machines in order to meet compliance requirements, you want to consider sole-tenant nodes. A sole-tenant node is a physical Compute Engine server that is dedicated to hosting VM instances only for your specific project.
- Use sole-tenant nodes to keep your instances physically separated from instances in other projects, or to group your instances together on the same host hardware, for example if you have a payment processing workload that needs to be isolated to meet compliance requirements.


## Preemptible VMs

- These VMs can be interrupted by Google at any time when they are facing resource scarcity at any Point of Presence.
- These VMs may cost 60% to 90% less than the regular ones.
- 30 second terminate warning with time for shutdown scripts (not guaranteed).
- No auto-restart, live-migrate, etc. However, there are external clever ways to actually keep starting VMs. Mandatory preemption after 24 hours.
- One major use case for preemptible VMs is running batch processing jobs. If some of those instances terminate during processing, the job slows but it does not completely stop. Therefore, preemptible instances complete your batch processing tasks without placing additional workload on your existing instances, and without requiring you to pay full price for additional normal instances.


## Spot VMs

- Spot VMs are the latest version of preemptible VMs. Spot VMs are virtual machine (VM) instances with the spot provisioning model. New and existing preemptible VMs continue to be supported, and preemptible VMs use the same pricing model as Spot VMs. However, spot VMs provide new features that preemptible VMs do not support. For example, preemptible VMs can only run for up to 24 hours at a time, but Spot VMs do not have a maximum runtime.
- Capacity for spot VMs is often easier to get for smaller machine types, meaning machine types with less resources like vCPU and memory.


## Shielded VMs

- Shielded VMs offer verifiable integrity to your VM instances, so you can be confident that your instances haven't been compromised by boot or kernel-level malware or rootkits.
- Shielded VMS is the first offering in the Shielded Cloud Initiative. The Shielded Cloud Initiative is meant to provide an even more secure foundation for all of Google Cloud by providing verifiable integrity and offering features, like vTPM shielding or sealing, that help prevent data exfiltration.
- In order to use the shielded VM features, you need to select a shielded image.
- Confidential VMs are a breakthrough technology that allows you to encrypt data in use, while it's been processed.


## Compute Pricing

- All vCPUs, GPUs, and GB of memory are charged a minimum of 1 minute. For example, if you run your virtual machine for 30 seconds, you will be billed for 1 minute of usage. After 1 minute, instances are charged in 1-second increments.
- Compute Engine uses a resource-based pricing model, where each vCPU and each GB of memory on Compute Engine is billed separately rather than as a part of a single machine type. You still create instances using predefined machine types, but your bill reports them as individual vCPUs and memory used. The discount is up to 70% for memory-optimized machine types.
- Preemptible and Spot VMs are instances that you can create and run at a much lower price than normal instances. For both types of VM, Compute Engine might terminate (or preempt) these instances if it requires to access those resources for other tasks. Preemptible VMs can only run for up to 24 hours at a time, but Spot VMs do not have a maximum runtime.


## Discounts

- There are several discounts available but the discount types cannot be combined. 
- Resource-based pricing allows Compute Engine to apply **sustained use discounts** to all of your predefined machine types usage in a region collectively rather than to individual machine types.
- For example, when you run one of these resources for more than 25% of a month, Compute Engine automatically gives you a discount for every incremental minute you use for that instance. The discount increases with usage, and you can get up to 30% net discount for instances that run the entire month.
- If your workload is stable and predictable, you can purchase a specific amount of vCPUs and memory for a discount off of normal prices in return for committing to a usage term of 1 year or 3 years. The **committed use discount** is up to 57% for most machine types or custom machine types.
- **Preemptible use discounts** may be availed by using those instances as well.
- To calculate discounts, the pricing calculator may be used.


## Labs: VM to Set up a Minecraft Server

Explores the process of setting up an instance, SSHing to install headless JRE to run the JAR binary of Minecraft and make a server out of the instance along with external persistent storage disks.