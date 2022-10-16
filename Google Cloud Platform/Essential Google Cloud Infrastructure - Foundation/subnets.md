# Subnets

- For every region, a subnet can be created. This also ensures that if a particular network has a subnet at any region, a resource allocated (of any type) may access that particular subnet for networking. They can cross zones.
- Every subnet has an IP range. The internal IP is alloted to a machine connected to that subnetwork within the given IP range. That itself is the identity of an instance - the subnet it is connected to.
- Large subnets should be avoided. They can expand but not shrink. The IP range mentioned should be a valid CIDR block. Also, a subnet cannot overlap with another. These are the basic rules that must be kept in mind while dealing with subnets.


## Subnet Expansion

Assume that we have a custom subnet with a /29 mask. This provides us with 8 IP addresses - 4 of which are already reserved by GCP and the rest are free for use by instances. When we create instances, we notice:
- 4 instances can be created with no error on that subnet.
- The fifth instances cannot be created since the subnet has been completely used up. So subnet expansion must be done now. <br />
For subnet expansion, we don't need to take down any running instances. We can just go over to the IP range of the subnet, change it from /29 to /23 (which gives us more than 500 instances to spin up in that subnet). That should do the trick. Now more instances can be created.


