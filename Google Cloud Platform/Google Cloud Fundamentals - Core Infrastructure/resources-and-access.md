# Resources & Access in Google Cloud

The first thing to learn before moving on to hands-on operations is the theory behind the access and resource management facilities in Google Cloud for large organizations.


## Resource Heirarchy

- There are four levels of heirarchy in Google Cloud:
1. Resource Level (level I): Any Cloud service such as *Compute* or *Storage* is at this level. Each resource belongs to only one project.
1. Project level (level II): Every resource sits inside the project in which it is created. There can be multiple projects that an organization creates. This may correspond to a part of the product that is being considered separately.
1. Folder level (level III): Every project sits within the respective folders that an organization has. This generally correspond to a product that is being manufactured by the organization. Used to represent heirarchies when needed and to enforce resource policies for the lower levels under it.
1. Organization Node (level IV): The final level at which the organization sits. They are optional in general but a must if folders are to exist.
- There exist Policies that apply to any of the 4 levels. We may have policies that apply to level 3 and level 1.
- Policies are downward inherited. So any policy added to the project level would also apply to the resources.
- The Projects in here are understood by three fields: the project ID, project name and project number. The name can be chosen by us and is mutable. It need not be unique as well, unlike the other two.
- The `Resource Manager Tool` is used as a RPC or a REST API to programmatically manage projects.


## Identity and Access Management (IAM)

- With so many levels of granularity already at hand, we need a singular and sophesticated mechanism to ensure that the allotment of services and their permissions of use are given to the right resources. Administrators may apply policies to restrict the people doing whatever tasks they do on certain services.
- The types of roles in IAM are:
  - Basic IAM
  - Predefined IAM
  - Custom IAM


## Basic IAM Roles

Very broad in scope and straightforward. When applied to a project, they affect all resources in the project. We must remember that basic roles are way too broad and not always recommended. In fact, for complex projects, they should be sparingly used.
1. Owner: Has every possible access.
1. Editor: Can only view and edit resources.
1. Viewer: Can only view resources.
1. Billing Admin: Can view resources and see costs.


## Predefined IAM Roles

The actions are very specific in here. We may be given an admin for a particular resource that we have to manage in a certain way. It is possible that such a role has been already made by Google for us. An example would be the Admin role for an instance.


## Custom IAM Roles

- If we want even more granular configurations and resource access, we have to set the roles in certain specific ways manually. This approach is taken by companies who offer the minumum amount of resources to the employees for use so that overuse would not happen, just to be on the safer side.
- Can only be applied to organizational or project level.
- The permissions need to be managed as well by the new policies.


## Service Accounts

- Service Accounts are systems maintained that allow us to set exclusive bounds and permissions to Google instances (or a group of instances) belonging to any service. 
- The fundamental difference is that the permissions are being given to a set of machines rather than the users. That fundamentally differentiates it from the basic implementation of IAM.
- **For example**, consider a VM that stores data in *Storage*. Only that VM is to access that data-store, nobody else. We can give the *Storage* instance certain permissions and restrictions. That can be done using service accounts.
- The are named with an email address and use cryptographic keys instead of passwords.
- Service Accounts need to be managed just like IAM.


## Cloud Identity

- With Cloud Identity, organizations can define policies and manage the user and groups using the Google Admin Console.
- This makes the entry and removal of a person joining or leaving the organization much simpler as the Admin can simply go ahead and disable or remove the user accounts.


## Accessing Google Cloud

- **Cloud Console**: The general console that we use.
- **Cloud Console Mobile App**: A mobile app that we can use just like the Console. It is a miniaturized version of the first option that can be used to start, stop or SSH into instances, see logs and several low-overhead use-cases.
- **APIs**: Using Google Cloud API endpoints upon having the API keys and necessary credentials for authentication.
- **Cloud SDK & Cloud Shell**: It is basically a Debian-based Linux instance with a 5 GB persistent directory that runs with a terminal and is equipped with all the required commands of `gsutil`, `bq`, `kubectl`, etc. They are always up to date.


## Lab: Bitnami's LAMP-stack

The goal of this lab is to explore the *Marketplace* to deploy a pre-made and configured instance that supports the LAMP stack. This shows us that *Marketplace* is a service from where pre-configured solutions for deployment being offered by various vendors can also be viewed.
Additional configurations can also be done on top of that like setting up the zone, region, instance names, instance hardware configuration, etc.
The charges would be displayed for a month.