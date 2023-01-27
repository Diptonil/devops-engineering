# Domain Name System

DNS translates human readable domain names (www.somewebsite.uk) to machine readable IP addresses (192.0.2.94).


## Why Not Just a Database?

When we are asked to build a system solution in which system hostnames are to be mapped to a more human-friendly, readable and business-promulgating domain names, the immediate solution that may come to our minds is to have a SQL database with one column as a hostname and another as a domain name. <br />
However, this database system breaks down due to:
- There are too many websites. Allotting a centralised, all-powerful machine that is 100% failsafe at all times throughout history is impossible, even with replications. This is because the load would be too much - literally every connection in the world would require a query to this very database.
- To optimize the database design, we need to resort to normalizations, which most often leads to more complications that the solutions it leads to, if done at higher forms. This is to remove redundancy in case of load balanced servers pointing to a same domain name. Moreover, designing foolproof normalizations are quite difficult.
- The hostnames might be ephemeral. There would be new hosts and old ones that get killed every second. So the database not only has to address queries, it also has to address insertions and deletions, whilst ensuring concurrency is safe.


## Domains

With every website (take 'www.blog.me.lit' as an example here), we have a domain split up into two (or three or more levels):
- **Top-level domain**: The namespace following the last dot. Examples: `org`, `edu`, `com`, etc. In this case, it is `lit`.
- **Second-level domain**: The `me` in the above example is a second leve domain. This is not compulsory for every website at all. Some do have it these days.
- **Subdomain**: The main name that is used to term the website (in this case it is `blog`) is known as subdomain. <br />
We would see how a DNS addresses the advantages of these levels of domains.


## Records

DNS Records can be understood to be a type of a data structure that has information about hostnames and domain. There are many types of DNS records but the primary 5 types are:
- **A Record**:
    - Most important. A stands for Address.
    - Shows the IP Address for a specific hostname.
    - A browser can load a website using the domain name. No IP Address needed.
- **AAAA Record**: AAAA record, just like A record, point to the IP address for a domain. However, this DNS record type is different in the sense that it points to IPV6 addresses.
- **CNAME Records**:
    - CNAME means Canonical Name.
    - This doesn't point to any IP address, but another domain.
    - Subdomains point to the their respective domains. So, broader heirarchial systems are resolved in such ways.
    - For example, the subdomain sub1.example.com can point to example.com using CNAME.
    - A practical example for the use of CNAME records is running multiple subdomains for different purposes on the same server. For example, we can use ftp.example.com for file transfer protocol (FTP) and serve webpages via www.example.com. We can then use a CNAME record to point both subdomains to example.com.
- **NS Records**:
    - Specifies the authoritative DNS server for a domain. In other words, the NS record helps point to where internet applications like a web browser can find the IP address for a domain name. Usually, multiple nameservers are specified for a domain.
    - For example, these could look like ns1.examplehostingprovider.com and ns2.examplehostingprovider.com (YesMovies is a nice example).
- **MX Records**:
    - It stands for Mail Exchange Records.
    - It shows where emails for a domain should be routed to. It directs emails to a mail server.
    - You can have multiple MX records for a single domain name (we can have multiple email servers with priorities assigned to them in precedence with respect to their capacities or use frequency (or some other metric)).
    - In most cases, if primary server fails, the secondary email server takes over. All that data is to be found in this record.


## Effectiveness of a Machine Acting as a DNS

The domain levels stated above are arranged in tiers as tree nodes. Therefore, if we see that a domain belongs to the top-level `.com`, we immediately fire off all other results in other domains like `edu` or `mil`, etc. Same happens with the lower level domains, until we reach a level where we only have subdomains. Billions of results are effectively removed. This is an example of effective partitioning. <br />
The above process continues through a tree of such machines from the root DNS node until we have the final machine that performs the translation.
This leads us to an understanding that perhaps rather than using a centralised fail-prone machine, we should go for a bunch of machines
since all are worth having and have their distinctive purposes. For each top-level domain, we can have an exclusive suite of servers that would work for translation of their domain names into their hostnames.


## Root Nameservers

- These servers are responsible for giving us the DNS servers that are responsible for all the top-level domains (like com, edu, etc.).
- These are 13 in number all over the world. They are all *replicated*.
- They have IPv4 addresses of themselves as well as IPv6.
- These themselves aren't associated in finding out all the domains under a particular name. They are just there to point and guide towards the top-level domain servers. It just gives back the IP address of a top-level domain that we are requesting.
- Once the client is to go to a particular website, first the domain name gets translated to the server it is actually supposed to make a connection to. This it does with the help of a root server.
- The communication of a host with the root DNS server to get back the IP address of the top-level domain servers is referred to as the **first-hop**.


## Top-Level Domain Nameservers

- There are many such servers. All are responsible for the handling of the com, net, edu, et cetera domains. Also known as TLD nameservers.
- Their job is to recieve a request from the host and return the IP address of another server that is actually responsible with the knowledge of the requested domain.
- This design is done because domains are added and taken off at all times. To be the routing machine of all top-level domains is responsibility enough. The servers aren't overburdened a lot like this.
- The communication of a host with this machine and the host is referred to as the **second hop**.


## Authoritative Nameserver

- This server has the answer to where a particular server is. The communication of a host with this machine is the **third hop**.
- With additions and removal of all hosts over the internet, this keeps track of them all. It is an extensive business.
- A-Record lookup occurs here.
- The address is resolved when this server performs a lookup in the A Record of the DNS. Now the final destination is known.


## Resolvers

- Before any of this even happens, the client would first send a *synchronised request* to a machine called *Resolver*.
- The *resolver* would send out *three synchronised requests* to all the 3 DNS servers one ofter the other. Finally, it gets back the result, which it sends back to the client.
- Now the client has the IP address of the machine it wants to connect to. So it can establish a TCP connection with the said machine and see the transaction through.


## UDP

This whole transaction is carried out through UDP. But the question is that since we are dealing with datagrams, we may not know which datagram belongs to which query made. To resolve this, every request has an ID that can be recognised. This prevents the datagrams from getting jumbled and has them routed back safely. <br />
There are, as with every technology over a network, many techniques that attackers employ to cause damage. DNS Poisoning is an important one. It mostly nvolves spoofing many UDP requests to the DNS so that at least one passes through and makes the client land in the malicious websites. They are explored in the Security.


## Problem With Distribution for DNS

Even though DNS is claimed to be distributed, there still exist a single point of failure that can kill the whole system. There is always a dependency chain that goes down right from the moment when the root DNS replies. So if the DNS pointed to is down, the requests fail. This has historically also led to many attacks. <br />
One of such attacks that can happen due to this dependency chain is that attacks may host their own servers to act as Authoritative nameservers.
