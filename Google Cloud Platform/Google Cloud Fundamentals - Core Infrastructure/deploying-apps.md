# Deploying Apps

Apps in Google Coud may be deployed in many ways. We can use the GKE to achieve extreme levels of granularity and low-level control of our resources. We may work with VMs for less demanding apps that need modularity in resources. We can also opt for services that let the Cloud completely handle our needs as we focus on the development rather than the deployment.


## App Engine

- This was the first Google Cloud product.
- We can easily choose libraries, languages and frameworks for the job. The Cloud will take care of the rest for us.
- It is, as easily observable, Product-as-a-Service offering by Google Cloud, like Heroku.
- Servers are provisioned and scaled automatically. We don't need to maintain. It can provide us health checks, caching, databases, application logs, load balancing and authentication without our intervention to configure any of these.
- We can use the Security Command Centre in conjunction with the App Engine to also be sure of the safety of our apps.


## App Engine Environments

- **Standard**
    - Preconfigured with the container instances running on Google's infrastructure.
    - Less manual control.
    - For many and most basic (since basic dominates the business environment) needs, the standard environment might all we need.
    - It has features like cron jobs, automatic scaling and load balancing, persistent storage with queries, sorting and transactions.
    - Only Java, PHP, Python, Node.js, Go and Ruby are supported as such. Apps must also conform to sandbox constraints dependent on runtime. This allows the engine to distribute requests across multiple servers.
    - No SSHing.
    - No writes to local disks. Runtimes can only access the `tmp/` directory.
    - Startup takes seconds.
- **Flexible**
    - We get to have a bit of more control over the services, even though all is managed at the end by GCP itself.
    - It supports microservices, databases, traffic splitting, logs, versioning, security, searches, ad everything else the standard plan supports.
    - We can use Dockerfiles as well for containerisation.
    - SSHing allowed.
    - Writes to local disks are allowed.
    - Startup takes minutes.


## API Management Systems

- **Cloud Endpoints**
    - Distributed API Management Systems.
    - API hosting, monitoring, logging are all provided.
    - Any API supporting the OpenAPI specification.
    - Supports apps running in GKE, App Engine, Compute Engine.
- **Apigee Edge**
    - They focus on specific business problems, like rate limiting, quotas and analysis.
    - Backend services for Apigee Edge don't have to be in Google Cloud. As a result, engineers also often use it to take apart legacy applications. Instead of replacing a large important application in one move, they can use Apigee Edge to peel off its services individually instead.


## Cloud Run

- A managed compute platform that can run stateless containers.
- Serverless. It means that infrastructure management is not needed (not to be confused with "it doesn't run on servers". It very much does).
- Built on Knative.
- Extremely fast.
- Developer workflow:
    - Write a web app that starts a server and listens for web requests.
    - Build and package the app into a container image.
    - Push the image to an artifact registry where Cloud Run deploys it.
- We can use both container-based workflows and source-based workflows.


## Cloud Development

- Google Cloud also provides tools to develop apps in the Cloud. This is an option for those who can afford such a convenience.
- *Cloud Source Repositories* is a versioning tool similar to Git for private collaboration within the Google Cloud environment that directly can intermingle with *App Engine* and *Compute Engine*.
- *Cloud Functions* is a great development tool that can be leveraged to deploy lightweight, event-based workloads that are aynchronous and serverless. We need not care about any infrastructure on which these are deployed. We just can rest assured knowing that it magically works. We get billed for 100 milliseconds.


## Cloud Deployment

- To set up a deployment, we need to be able to write commands particular to the configuration of the framework that we have used to write our app.
- This process is extremely labour-intensive and makes deployments a pain. To ease this, certain tools are created - templates. We can just deploy our app using these templates.
- Terraform is a tool by Hashicorp that uses HCL (Hashicorp Programming Language) that does just that.


## Lab: Introducing Cloud Run & Terraform

1. Build a simple containerized application image and deploy it to Cloud Run.
1. Make a Terraform configuration with a module to automate the deployment of Google Cloud infrastructure.