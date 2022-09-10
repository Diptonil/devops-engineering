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


## Quiz

1. When would you choose to have an organization node? (Select two)
- [x] When you want to create folders
- [ ] When you want to organize resources into projects
- [x] When you want to centrally apply organization-wide policies
- [ ] There’s no choice; organization nodes are mandatory.
2. Which statement best describes how Google Cloud resources are associated within the resource hierarchy?
- [ ] All Google Cloud resources are associated with an organization.
- [ ] All Google Cloud resources are associated with a folder.
- [ ] Google Cloud resources are not associated with the resource hierarchy.
- [x] All Google Cloud resources are associated with a project.
3. Consider a single hierarchy of Google Cloud resources. Which of these situations is possible? (Choose 3 responses)
- [x] There is no organization node, and there are no folders.
- [ ] There is no organization node, but there is at least one folder.
- [x] There is an organization node, and there are no folders.
- [x] There is an organization node, and there is at least one folder.
- [ ] There are two or more organization nodes.
4. Your company has two Google Cloud projects and you want them to share policies. What is the least error-prone way to set this up?
- [ ] Duplicate all the policies from one project onto the other. 
- [x] Place both projects into a folder, and define the policies on that folder.
- [ ] Create shared resource policies on the common resources that are used in both projects.
- [ ] Define the new shared policy in the organization node.
5. What is the difference between Identity and Access Management (IAM) basic roles and IAM predefined roles?
- [ ] Basic roles only allow viewing, creating, and deleting resources. Predefined roles allow any modification.
- [x] Basic roles affect all resources in a Google Cloud project. Predefined roles apply to a specific service in a project.
- [ ] Basic roles can only be granted to single users. Predefined roles can be associated with a group.
- [ ] Basic roles only apply to the owner of the Google Cloud project. Predefined roles can be associated with any user.
6. Select the option that displays IAM roles from general to specific. 
- [ ] Custom roles, predefined roles, basic roles
- [ ] Predefined roles, custom roles, basic roles
- [x] Basic roles, predefined roles, custom roles
7. How does the resource hierarchy control how IAM policies are inherited?
- [ ] IAM policies that are implemented higher in the resource hierarchy deny access that is granted by lower-level policies.
- [x] IAM policies that are implemented by lower-level policies can override the policies defined at a higher level. 
- [ ] IAM policies are only implemented at the project level; they cannot be amended by lower levels of the resource hierarchy.
8. Which way of accessing Google Cloud lets you control services through the code you write?
- [ ] The Cloud Console
- [ ] The Cloud SDK and Cloud Shell
- [x] APIs
- [ ] The Cloud Console mobile app