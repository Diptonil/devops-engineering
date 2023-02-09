# Database Replication

- When we are using a database instance, we are making reads and writes to it concurrently. Even if all the queries that we are doing are perfectly optimized, there occurs a stage of saturation beyond which the physical resources associated to that instance would start too wear thin. This brings in the concept of replication.
- It is the process of having multiple instances of the same database paradigm representing that same data model.
- There are multiple possible implementations. The common factor here is that we have a primary instance that is capable of handling reads and writes both. Then we have multiple replicas - secondary instances that can only serve writes.


## Statement Based Replication

- The brute force method would be to send the write SQL statements to *all* the replica instances so that they could update themselves.
- The bandwidth requirement is quite low here since we are just sending in the string of the query.
- The approach seems to work fine but then we are just spending time to *plan* and *execute* (which are different things) the same query in every instance again and again. This is expensive with respect to time. We can do much better.
- We do experience a certain delay in the committing of the changes. So, our systems aren't *exactly* consistent since it takes time to propagate all changes. This is eventual consistency because ultimately, it would take some time for the system to become consistent eventually.


## Binary Replication

- Instead of sending the query statement to the databases, we send the *output* of the statement in bare binary terms that the system would understand quicker.
- We can ship these binaries by streaming. This makes it a binary streaming replication.
- This makes rollbacks quite difficult to execute. Because all the changes are just send and already committed.
- This is also eventually consistent.


## Logical Replication

- This is something that PostgreSQL does. Instead of working on the binary data, they push the logical changes in simpler terms, consuming low bandwidth in a way that makes sense to the database.
- Had binary changes been pushed, a PostgreSQL 10 version database might have difficulty processing a PostgreSQL 14 binary.
- We can also ship logical changes via streams. This makes it logical streaming replication.
- This is also eventually consistent.


## Synchronous Replication

- We have seen examples of eventual consistency in the previous techniques. Here, we achieve actual consistency in replication.
- CassandraDB was the one to actually do this.
- We get an updation, creation or deletion execution on our primary. It doesn't return immediately to service the user again. It goes and sends the request to the other replicas and awaits a confirmation for commit from their end. If all confirm, it commits to itself and then returns to the user with the updation.
- This meant we are always going to see consistent values of our data, despite us losing availability of databases for a few seconds (as per CAP).


## Asynchronous Replication

This gives faster commits in a distributed database environment but are all ultimately eventually consistent since changes are propagating through. System is available at all times.


## One Way Replication

This technique can allow writes only to the primary machine. All others are marked as secondary read machines without write privileges. It causes trouble when we want to scale out our writes.


## Bi-Directional Replication

This technique can allow writes to the replicas as well. Which is a drastic measure since different techniques of conflict resolution also comes into the picture. <br />
The techniques are a different concept in themselves (similar to how Kafka handles things).