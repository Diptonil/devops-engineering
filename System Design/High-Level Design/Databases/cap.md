# CAP Theorem

CAP stands for Consistency, Availibility and Partition Tolerance. This particular theorem is vitally important to make us clear design decisions when it comes to distributed systems. <br />
CAP theorem applies to distributed databases - a single representation of data backed by several nodes or machines (that live in a black box).


## Consistency

- It basically means that when we do a write to the database at a single node, the change caused by that write must be visible across all nodes so that when a read is done *right* after that change, the updation must be visible.
- Not all systems are consisten, even it might seem so. At certain times when we do a write to the master node, the change may take some time to propagate through the worker nodes. This does happen in Redis cache systems or Memcached.
- **Eventual Consistency** is a guarantee that when an update is made in a distributed database, that update will eventually be reflected in all nodes that store the data, resulting in the same response every time the data is queried. The changes don't reflect soon enough is what they mean by that and it seems to almost be an excuse for being inconsistent. So many engineers don't like this term.
- Some engineers do treat consistency as absolute. No eventual consistencies.


## Availibility

- It basically means that reads and writes are guaranteed to succeed at all times. Doesn't matter if the results are wrong.
- We can make systems available by adding more caches but it comes at the cost of consistency, of course (caches may store stale data).


## Partition Tolerance

- It is important to know that this has *nothing* to do with database partitioning at all.
- It basically means that a network is partitioned when the nodes of a database cannot talk to each other. This essentially gives rise to failures in system. If we have a failure, in simple terms, we have a network partition.
- We may choose to have partitions or not. Absolutely *not having* any partitions at all actually means that we have one single, beefy machine that has no point of failure with respect to connectivity to other database instances. Allowing partitions means that we have multiple nodes (not too beefy), but acknowledging the fact that we may have partitions.


## The Theorem

The theorem states that if we have a chance of partitions in our systems, then our system would either be available or consistent. We cannot have both. <br />
This by extension means that we may have, at a given time, two out of the three tenets of availibility, partition tolerance or consistency.


## Example

Assume we have a primary master nodes and two secondary replica nodes. We choose to have a networked system, and hence are tolerating partitions.
- To ensure consistency: When a write is made to the master node, we block off all other client connections to the database and enure that the change is committed. So, the user can only ever see the updated values. This also means that the database would remain inaccessible till the time all the changes propagate to the worker nodes. So, we can never achieve availibility.
- To ensure availibility: When a write is made to the master node, we immediately issue an ACIDified transaction across the entire system. The written changes propagate throughout. But that also means a value can be read from the database that is old. So the value isn't actually updated. So, we can never achieve consistency.


## Being Consistent and Available

- Have a single, huge machine. We have no chance of network partitioning here, at least. So we can guarantee our system to be available at all times and even consistent since no changes need to go down any nodal heirarchy.
- The thing with CAP is, though, that it really depends where we are looking at it. We may inevitably have disk partitioning within a node (when we take the discussion outside the distributed system). In that case, if some wiring failure occurs, are we really consistent?


## YouTube Preferring Availibility in 2006

When YouTube had scaled out its MySQL nodes back in 2006, when we used to create a new user, after filling out the long form when we hit submit and then refresh, we weren't shown the actual changes that we made but still the old version. <br />
The creator had explained to the users then that it happened because they needed to stay available at all times.
