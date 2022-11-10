# MongoDB

The first thing to know about Mongo is that it is not a traditional RDBMS (like PostgreSQL; refer to that section to understand what an RDBMS is). It is built with the key design choice of a *document model*. An RDBMS has the feature of having data represented in tables that are linked to each other by various fields.  <br />
MongoDB's design principles make it highly compliant and geared towards a Cloud-native development. This has led to MongoDB being used in the Cloud (or its concepts in many different forms as different offerings by the CSPs). However, the recent popularity of MongoDB has led them to launch a new Database as a Service (DaaS) offering named as **MongoDB Atlas**, which enables csutomers consume MongoDB without worrying about the management overhead.


## Cons of RDBMS

- Representation of data is hard to understand.
- Pulling data in so many different tables is inefficient.
- Addition of data can be quite difficult since a lot of changes must be made to the remaining tables.


## Types of NoSQL Databases

MongoDB is essentially a NoSQL database. There are primarily 4 classes of a NoSQL service:
- **Key/Value database**: The store data with respect to unique keys to which they associate data. Data lives as a key-value pair. Keys can be kept in different servers to maintain a distributed database scheme.
- **Graph database**: Here, relations are maintained between objects in the same table rather than across tables.
- **Column oriented database**: Here, data is stored per column. It is great for analytics.
- **Document database**: This is what MongoDB is. This paradigm acknowledges that data is polymorphic by nature. These databases are made in a way to minimise time required to model databases and just focus on building application functionality first.


## MondoDB as a Distributed Database

Legacy databases are often backdated in their approach to provide a database system. The databases provided by them are mostly clustered on a single machine. MongoDB is a *distributed database*. This means that a single database runs on multiple different systems. Th pros that it gives:
- **Fault Tolerance**: A single point of failure doesn't bring down an entire database. Copies of data are stored on different machines at the same time, ensuring redundancy.
- **Scalability**: It is built on the principles of scalability, which means that it can scale into multiple servers at times of high loads and then shrink down into less servers when the spikes go down.
- **Move Data**: It lets us move data to keep it near the users for fastest access.


## Terminologies

Here are certain terms that are used in MongoDB, mapped to their SQL equivalents for ease in understanding.
- **Collection**: Table
- **Document**: Row
- **Field**: Column
- **Embedding, Linking, $lookups**: Joins
- **Read Only View**: View
- **Multi-Document ACID Transaction**: Multi-Record ACID Transaction
- **Array**: Parent-child tables


## MongoDB Arrays

A table has a relationship to other tables, relations like one-to-one, one-to-many, or many-to-many by linking attributes from both tables.

MongoDB can express the relationships between collections similarly. However, MongoDB has an additional feature, the ability to take the fields of child table and embed it with the parent table as a single collection.

This grouping leads to a data model with far fewer collections than the number of tables in the corresponding relational model.


## MongoDB Indexes

In RDBMS, indexes are built on any number of columns in a table.

In MongoDB, because there is far less need to bring data together, indexes are mainly used for filtering and sorting, rarely for joining. This leads to lower memory usage for indexes.

Building an index on a set of fields in a collection is the equivalent of having an index that would be built on a set of columns in a table.


## MongoDB Embedding & Linking

Joins are used in a relational database to get data from two or more tables.

With MongoDB, there is a $lookup operator to perform the same link between collections.

Additionally, some relationships are also expressed by embedding the child table in the parent table. For these relationship, there is no need to use the $lookup keyword, as the data is already pre-joined in the document. The document model makes things much natural and queries so much simpler.


## BSON

MongoDB database modelling is done in a way similar to writing JSON. Under the hood, however, it uses Binary-JSON (BSON). A lot of subtleties could be added to plain JSON in that way. For example, JSON only supports numbers. Here in MongoDB, there exist long, float, int, decimal, etc. data types.


## Distributed Systems Considerations

As compared to standard one-node database systems that were traditional, the model of MongoDB that has multiple servers with processes talking to each other at all times, there are certain important considerations for this model.
- **The Replica Set**: A Replica Set has three servers, which makes it highly available. Each have a complete copy of the entire database. The replication is automatically tracked and handled by MongoDB by tracking all writes to the primary database server and applying them to the secondaries. Selection of a primary can be automatic as well.
- **The Sharded Cluster**: Sharding is the technique to partition a database into many servers. We might do this for two reasons: either to place data close to the users or to handle large datasets.
- **The Global Cluster**: If we want our workloads to be situated globally across multiple different geographic regions, we can use the global cluster. It is quite easy to provision one in Atlas but can be manually configured as well.


## Operation Guarantees

The CAP Theoren states that a distributed database can have, at a given time, only two of these, but not all three:
- Consistency
- Availability
- Partitioning <br />
To support all three of these requests, MongoDB has:
- Write Concern: Contract of durability when writes happen between the MongoDB server and the application.
- Read Concern: Works in conjunction to the write concern.
- Read Preference: The preferred node to read from.


## ACID for MongoDB

Basic database system design deals with the concepts of ACID compliance, which stands for:
- **Atomicity**: Transactions are all or nothing. This is done here by ensuring that all writes to one document are done at once.
- **Consistency**: Data must be valid to be saved. No dependency on other documents.
- **Isolation**: Transactions do not affect each other. Document being modified is unseen by other reads.
- **Durability**: Written data will not be lost. Guaranteed by doing a write with a 'majority' concern. <br />
They are applicable for sharded database systems as well.


## Modelling in MongoDB

- In MongoDB, emphasis is on workloads when starting out with the design and modelling of the database. For SQL, it was on ER diagrams.
- Normalization is a big part of SQL-based systems. However, the only thing that matters here is simplicity and performance.
- To define a MongoDB schema, we need to follow these steps:
    - **Describe the Workload**: Here we understand what we are modelling for, quantify and qualify read and write operations, make a list of all operations that are important.
    - **Model the Relations**: It is similar to relational modelling of one-to-one, one-to-many, many-to-many relationships; we choose if we would like to embed in the same documents or reference or link to some other document.
    - **Apply Patterns**: Patterns are some conventional design choices to achieve some maintenance and performance boosts or address simplicity.
- **Staleness of Data** is the state when some data gets somewhat old and falls out of consideration. At times, it may be acceptable. Stale data is usually okay for instances when the data is not being used for current trend measurement or latest analytical surveys.
- **Sizing**: We take a look at the size of the dataset to decide if we should shard or not.
- **Embedding or Referencing**: Embedding is putting the child element within a parent element (no need for primary keys for children or foreign keys for parents) while referencing is putting the two entities separately (primary and foreign keys are needed). Embedding should be the default choice because that is the defining factor of MongoDB. We should reference if the number of child entities grow out of hand or for integrity on write operations for many-to-many relations, as a basic rule of thumb.


## Database Documents

Here are a few examples to illustrate how databases are made in MongoDB:
1. 