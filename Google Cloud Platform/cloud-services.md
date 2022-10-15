# Cloud Services

A basic overview of the important services can be understood here:

- *Compute Engine*: The most basic service in Cloud is this. It is the service that is known by most others. It is used to set up and run a basic VM on the cloud that can be tailored by users for their own use. It can be utilised as a server, a platform for debugging, etc.
- *Google Kubernetes Engine*: We can run containerized applications in Google by leveraging this service. Using VMs to start up Kubernetes and Docker services is tedious. Spinning up clusters can be easily made with this service. Moreover, the Cloud Console can be used seamlessly to integrate with the complexities to manage and deploy a cluster.
- *App Engine*: It is a PaaS archiecture product that can easily be used to deploy a web app such that the users don't need to worry about the nuances of resource and hardware management. Google takes care of that behind the scenes. Users can just write code, configure some minimum settings and deploy their apps.
- *Cloud Functions*: It is a completely serverless service that can be used to deploy a piece of code on a server. We can just magically expect it to run. We do not have to worry about the infrastructure and servers. Google takes care of that for us. Resources are scaled as per requirement. A famous use-case is the handling of certain tasks when a certain event is triggered.
