# Redis

Redis stands for Remote Dictionary Server and is used as an in-memory database. That basically means that the storage happens on RAM directly and there is no secondary storage involved in any way. This leads extreme gains in terms of performance when used properly. This is also the reason why Redis has become widely used as caches over larger relational or NoSQL databases. This is in fact a common use case of Redis. <br />
Another main use-case of Redis is that it actually may also be used as a fully-fledged database facility that can store all formats of data.


## Challenges of Multiple Data Services

- Assume we are running a social-media app based on Microservices. The data model would be something like this:
    - **Relational Database**: To store user data with various relations to other fields. Example: MySql.
    - **Document Database**: To store media files in structure. Example: MongoDB.
    - **Graph Database**: To maintain user connections and relations. Example: Neo4j.
    - **Full-Text Search**: To provide a mechanism for searching of all textual material. Example: ElasticSearch.
    - **Cache**: To reduce fetch latency. Example: Memcached.
- Every microservice would interact differently with all of these in many different ways. This increases overhead.
- Even though these models in themselves may be very fast, there is significant latency in exchange of data due to network hopping. There is slowing down due to this as well.
- Getting so many managed services from the Cloud providers is an extremely expensive option.
- Configuring so many services and models together perfectly is a challenge.
- The microservice code needs to be updated and configured very carefully to avoid misconfigurations.


## Redis Modules

- Redis Core is primarily a key-value pair store.
- To store different formats of datalike search engines, graph storage, Redis Core extends modules.
- The Redis Modules are different services such as RediSearch, RedisJSON, RedisGraph, etc. These are modular and we can choose what we want for our project. They aren't tightly integrated and bundled to each other.
- Redis Modules is what makes it possible for Redis to be more than just any other database service because it comes with tonnes of functionalities. Different data formats can be incorporated in this way.


## Multi-Model Databases

Redis is such a kind of database. The properties that it offers over the Multiple-Service model:
- Using only one database instead of multiple data services.
- Simple configuration due to presence of only one service.
- No network hopping to deal with data transfer between services.


## Data Persistence

Since Redis is in-memory, obviously all data would be gone as soon as the system shuts down. To prevent this, we have to keep the system on at all times and some solutions are:
1. **Replication**: A master node is replicated into several other nodes. If one node goes down, the other remains working.
1. **Snapshotting**: Single file point-in-time snapshots of the dataset is stored on disk as a .rdb file. This is good for backup and disaster recovery. The problem is that we may lose the last few minutes of data.
1. **Append Only File**: The principle is to log all write operations to the disk continuously. This is more durable but is slower than snapshotting. *This is what Redis uses primarily.* <br />
We can use the combination of both as well. Redis expects to migrate to a model in which the combination is used.


## Storage of AOF

The Append Only Log Files need to be stored somewhere as they get generated. Storing on the server than runs Redis is an option but a bad one because it is best practice to separate out server that hosts an application and the server that is associated to store all its generated data.<br />
If Redis were to be hosted on EC2 instances on AWS, we would use an EBS instance to store all the generated data. So, we can also have recovery and durability with Redis in such ways.


## Redis on Flash

We can see that if we are to use an in-memory database, for obtaining a storage that is large enough, we would have to incur extreme amounts of costs. This is the tradeoff of using Redis. To optimize costs, however, we have Redis on Flash. Flash is a part of the Redis enterprise. <br />
Basically, it extends the RAM into the SSDs. The hot values (frequently accessed) are towards RAM. The more infrequent values are pushed towards the SSD. This means that we can make use of an entire machine infrastructure rather than just accessing its RAM (which is the standard Redis feature). This lowers cost.


## Scaling Redis

We may incur instances such as an instance becoming a bottleneck (too many requests) or instance running out of memory. The solutions to scale Redis:
1. **Clustering**: We may have a primary node for writing data and many other replica nodes for reading data in a cluster. Availibility is increased and redundancy is also ensured.
1. **Sharding**: This relates to the concept of database sharding in which data is taken and split up into parts (shards). Those shards are sent over to the different distributed instances. Shards take up less memory. <br />
So we have multiple nodes that have multiple replica and are sharded. This is the design of Redis in terms of scalability. Managing this ight be tedious by oneself. The managed services like Redis Enterprise or the Cloud providers would provide solutions to this.


# Geographic Scaling

We would want two things:
- Distribution of the instances across the globe to support users from multiple regions.
- Points for disaster recovery. <br />
To ensure this, we look into geographic scaling. So we basically want instances being able to read/ write data that are in sync with each other. To do this, we have Redis clusters. They are in sync with each other and spread all across the globe. They act as local instances for requests incoming from their region. The Sync is a *compressed and secured stream*. Syncers contact their masters for replication.


## Conflict-Free Replicating Data Types

To resolve conflicts made to the same datasets across different regions (in different clusters), we use CRDT. It is somewhat of a versioning system in Redis for all the changes that occur. Dataset eventually does converge to a single and consistent state. None of the changes, in this way, are lost.


## Pros

- One of the fastest database services.
- Offers multiple additional services equivalent to ElasticSearch, relational and non-relational databases, graph databases, etc.
- Redis is schemaless. So test database doesn't need to be initialised. This speeds up tests.
