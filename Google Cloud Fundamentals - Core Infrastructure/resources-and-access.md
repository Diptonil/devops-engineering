# Resources & Access in Google Cloud

The first thing to learn before moving on to hands-on operations is the theory behind the access and resource management facilities in Google Cloud for large organizations.


## Resource Heirarchy

- There are four levels of heirarchy in Google Cloud:
1. Resource Level (level I): Any Cloud service such as *Compute* or *Storage* is at this level. Each resource belongs to only one project.
1. Project level (level II): Every resource sits inside the project in which it is created. There can be multiple projects that an organization creates. This may correspond to a part of the product that is being considered separately.
1. Folder level (level III): Every project sits within the respective folders that an organization has. This generally correspond to a product that is being manufactured by the organization. Used to represent heirarchies when needed and to enforce resource policies for the lower levels under it.
1. Organization Node (level IV): The final level at which the organization sits.
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

- If we want even more granular configurations and resource access, we have to set the roles in certain specific ways. This approach is taken by companies who offer the minumum amount of resources that can be used at a time just to be on the safer side.
- Can only be applied to organizational or project level.
- The permissions need to be managed as well by the new policies.


## Service Accounts