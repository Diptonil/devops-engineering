# Containers in Cloud

Containers play a huge part in micro-management and use of softwares with multiple dependencies in a single place without necessarily having all those dependencies installed and just having tools to run and orchestrate containers. <br />
For more details on containers, consult the sections involving Docker and Kubernetes in this repository. In fact, it is highly recommended to first browse through those materials before landing here because this part completely builds on to the theory of Docker and Kubernetes.


## Pros of Using the GKE Model

- Easier to set up and run as compared to VMs.
- As app scales up, bare VMs start costing more if used to scale up. Containers and its resourceful management may lead to proper costs.
- The *App Engine* is sufficient for services that are classically designed and have medium traffic. It does not allow any customisation or granularity in handling. The *Google Kubernetes Engine*, on the other hand, does the job well.


## Hybrid or Multi-Cloud

- Enterprise systems these days are mostly distributed in architecture. Typical on-premises architectures have all servers running on the facility itself on the network of the companies. Long story short, these types of architectures are only preferrable for companies that have been in business for a long time since their growth is predictable. They only need resources on a more permanent basis. Most businesses have short-term requirements of resources. They benefit from Cloud.
- *Modern Hybrid Architectures* work on the principle of bringing in only some compute workloads over to the clouds. Parts of the system infrastructure remains and flexibility to choose Cloud services to meet their requirements is considered.
- This is a very good proposal to adopt distributed systems and services.
- *GKE On-Prem* is the GKE's on-premises counterpart. Whilst the GKE is itself a managed Kubernetes engine that runs on the Cloud, this ervice gives production-based performance not relying solely on the Cloud.


## Anthos

- Anthos is a hybrid and multi-cloud solution powered by the latest innovations in distributed systems and service management software from Google. It rests on the GKE and Kubernetes technologies.
- Its strength lies in the fact that it has a rich set of tools to monitor and maintain services and status both on-premises and on Cloud.
- To maintain an architecture with both *GKE* and *GKE On-Prem*, we have the *Marketplace* as a middle-man that acts as a third-party integration over both these layers.
- *Cloud Interconnect* is used to keep service meshes in sync.


## Lab: GKE's Introduction

Here we just need to create a cluster with three nodes initially. We just need to resize it to 4 nodes and create an Nginx web server deployment.