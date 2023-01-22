# Domain Name Service


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


## Effectiveness of a Machine Acting as a DNS

The domain levels stated above are arranged in tiers as tree nodes. Therefore, if we see that a domain belongs to the top-level `.com`, we immediately fire off all other results in other domains like `edu` or `mil`, etc. Same happens with the lower level domains, until we reach a level where we only have subdomains. This is an example of effective partitioning. <br />
This leads us to an undertsanding that perhaps rather than using a centralised fail-prone machine, we should go for a bunch of machines
since all are worth having and have their distinctive purposes. For each top-level domain, we can have an exclusive suite of servers that would work for translation of their domain names into their hostnames.


## Root DNS Servers

- These servers are responsible for giving us the DNS servers that are responsible for all the top-level domains (like com, edu, etc.).
- These are 13 in number all over the world.
- They have IPv4 addresses of themselves as well as IPv6.
- 