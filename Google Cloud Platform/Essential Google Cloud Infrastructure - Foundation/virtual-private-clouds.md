# VPC

A VPC network is a global resource that consists of a list of regional virtual subnetworks (subnets) in data centers, all connected by a global wide area network (WAN). VPC networks are logically isolated from each other in Google Cloud.


## Points of Presence

- Regions are the dominant places in a geographical region that can get devided into Zones. Apart from Iowa (that has 4 zones), all other regions have three zones.
- Closer availibility of clients to the regions where the servers of any application are located would mean faster connectivity. This is also ensured by extensive networking and presence of multiple Points of Presence.
- Networks are the connections between regions and zones that are physically laid by fibre-optic cables.


## Networks

- It is a global resource that spans all the available GCP Points of Presence. It is of three types (as shown in the lab). It has no IP address range, unlike subnets.
- It can contain any number of subnetworks to divide and segregate traffic routes.
- Instances in the same network (may be in different regions, doesn't matter) can connect to each others' intenal & external IP. To connect to the internal IP, firewall rules should be configured appropriately.
- Instances placed on different networks should be able to connect to each other (even if they are in the same region) only through external IP.
- Five networks is the default quota for each project.
- For knowing more about subnets, consult the `subnets.md` section.


## Routes

- Routes tell VM instances and the VPC network how to send traffic from an instance to a destination, either inside the network or outside Google Cloud. Each VPC network comes with some default routes to route traffic among its subnets and send traffic from eligible instances to the internet.
- There would be no routes without a network. They are created when a subnet is created.
- A network has two types of routes: *defined routes* that have actual guidelines associated to deliver traffic to and from instances as well as *default routes* that direct packets to destinations outside the network.
- Just creating routes don't mean that traffic would be delivered. Firewall rules also exist to allow ingress and egress.


## Firewalls

Each VPC network implements a distributed virtual firewall that you can configure. Firewall rules allow you to control which packets are allowed to travel to which destinations. We can restrict ro allow access to traffic on a particular machine using these rules. They are stateful. <br />
The implied firewalls allow all egress and deny all ingress. The default ones are:
- `default-allow-ssh`: Allows an instance to accept SSH connections. Anyone having a proper private key in any network can SSH. To reduce the scope down to some people in the subnets, we can tweak the rule.
- `default-allow-rdp`: Allows an instance to be connected via RDP (a proprietary protocol developed by Microsoft).
- `default-allow-internal`: Allow incoming traffic from VM instances in same network.
- `default-allow-icmp`: Allow Incoming ICMP from any source on the network.


## The Default Network

Every project under GCP has the default network provisioned already. That is how we can easily create VMs. Had that not been there, we would not be able to provision any other instances since there would be no connectivity.
- The default network has a managed system of routes preconfigured but we also may configure custom routes on our own.
- There are 4 default ingress rules that the default network has: `default-allow-icmp`, `default-allow-rdp`, `default-allow-ssh` and `default-allow-internal`. <br />
These firewall rules allow ICMP, RDP, and SSH ingress traffic from anywhere (0.0.0.0/0) and all TCP, UDP, and ICMP traffic within the network (10.128.0.0/9). The Targets, Filters, Protocols/ports, and Action columns explain these rules.
- This network provides the least amount of granularity and convenience to make it cater to our individual needs. But it can get the job done without making us think too much.
- It has one subnet per region.


## The Auto Mode Network

- Auto mode networks are easy to set up and use because they automatically create subnets in each region. However, you don't have complete control over the subnets created in your VPC network, including regions and IP address ranges used.
- Subnet masks can be expanded from /20 to /16.
- They allow some granulatity over the usual default network. We can choose from readymade firewalls, regions ato hook our subnets from, etc. - This mode of network is not recommended for use in production.
We can just leave all defaults as they are and create an Auto Mode network in case we ever lose the default network. Both are exactly the same.


## The Custom Network

An Auto Mode Network can easily be converted into a Custom Network just by altering a few of its settings. It provides more privileges to fine-tune and adjust connection needs and systems accordingly. It is always recommended that this setting is used in the production environments. <br />
They cannot be changed back to auto-mode networks, even if the vice-versa case is possible.


## IP Addresses

Every instance or machine has two types of IP Addresses. We must know that operations relating to external IPs may most probably cost us:
- **Internal IP**: This is the private IP that every instance has, given by the DHCP, allocated from the subnet range to VMs. The DNS is responsible to translate the hostname to the internal IP address. This address is compulsory for all machines for connection to the internet. We have provisions to actually tweak the internal IP address of the machine that we create for our convenience.
- **External IP**: It is a public IP address tht can be static or ephemeral (depending upon the choice). It is optional. It is required when our instances are facing external connetions. If we go for ephemerals, every time the instance restarts, we lose that previous IP address (but we also save on costs - static IPs cost more). Also, we cannot SSH to a system without an external IP.


## Mapping IP Addresses

Regardless of what the external IP address may be, it is always mapped to the internal IP. And each instance has a hostname that is mapped to the Internal IP address.
- Hostname is same as the instance name. Example: my-server.
- Name resolutions into addresses are handled by DNS.
- Lookup tables generally handle resolutions of external and internal IPs.
- We can also use IP aliasing in case we want to route traffic to a subnets but we have too many connections and many addresses are already hogged.


## Network Pricing

Pricing is subject to change. Therefore, this part is useful only to gauge *where* exactly costs go up when using networks. This is important to know because while creating networks, it is fairly easy to overlook price considerations since we do not get estimated prices like we get with *Compute Engine*.
- All ingress is free of cost (assuming services like Load Balancers are not a part of the design yet. If they are, prices are calculated based on that service).
- Egress to the same zone (internal IPs) and Google products are free of cost.
- Egress to the same zone (external IPs) is $0.01.
- For each GB of data, egress between zones in a same network is $0.01.
- Egress between regions has variable costs.
- Static and ephemeral attached to forwarding rules are free.
- Assigned but unused static IP addresses cost $0.01.
- Static and ephemeral used by standard VM instances cost $0.004.
- Static and ephemeral used by preemptible VM instances cost $0.002.


## Common Network Designs

- If the application needs *increased availability*, you can place two virtual machines into multiple zones but within the same subnetwork. Therefore, by allocating VMs on a single subnet to separate zones, you get improved availability without additional security complexity. A regional managed instance group contains instances from multiple zones across the same region which provides increased availability.
- If an application needs *increased globalization*, putting resources in different regions provides an even higher degree of failure independence. It is somewhat similar to the previous architecture where a certain degree of fault tolerance is observed (albeit localised).
- If an application needs *lesser user latencies*, using a load balancing service might be preferrable. This lets us route the traffic to the region closest to the user.
- As a general security best practice, assigning only internal IP addresses to VM instances whenever possible is appreciated. This applies for when the VM instances are acting as app servers. External IP addresses shouldn't be used in that case. The *Cloud NAT* is another service that provides address translation. It lets you provision your application instances without public IP addresses while also allowing them to access the Internet in a controlled and efficient manner.
- For private instances on a network, we should enable Private Google Access so that it can access all the Google APIs and services.


## Lab 1: VPC Default Mode, Auto Mode & Custom Mode Networking

Exploring all three types of networks in GCP - default, auto and custom networks.


## Lab 2: Using Cloud NAT

Here, we explore Private Google Access and Cloud NAT for a VM instance that doesn't have an external IP address. Then, you verify access to public IP addresses of Google APIs and services and other connections to the internet.