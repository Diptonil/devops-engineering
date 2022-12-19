# Storage Solutions

The Storage solutions provided by Google ranges from Structured, Unstructured, Relational and Transactional data storage. There are various services available to do these jobs.


## Cloud Storage: Basic Idea

- Treats data stored as objects, not blocks or files. They are organised within storage buckets. This is the **Object Storage** model. **File Storage** model stores data heirarchially as files within directories. **Block Storage** model stores data as chunks of disks.
- Objects have three forms of data - the binary containing the actual data, a globally unique identifier and metadata. They are then made available using URLs.
- It can be used for BLOB (Binary Large-Object) storage. Each object can have a 5 TB size.
- The ideal way to choose the region for this service is to pick a location closest to the user base to minimise latency.
- Any file that gets edited in the bucket doesn't get overwritten as the objects are immutable. A new one is created. Administrators may enable versioning to keep track of all the old data as well but if not, the previous object gets lost.
- To ensure best security practices, IAM roles may be used to limit the permissions of users with respect to te resources they access. To ensure even greater flexibility, Access Control Lists (ACLs) need to be used to define scope and permissions.
- **Lifecycle Policy** is a feature that allows us to determine the lifecycle of an object in a bucket (example: delete all objects older than 365 days, keep only recent 10 objects). This can help us manage costs as well.


## Cloud Storage: Storage Classes

There are 4 classes of storage:
1. **Standard Storage**: This is meant for frequently accessed/ writen to, 'hot' data. Also for data that is used for a short while.
2. **Nearline Storage**: This is meant for data accessed/ writen to about once or twice a month. This is good for frequent archives and backups.
3. **Coldline Storage**: This is meant for data accessed/ writen to about once every 3 months. The cost is significantly lower than the other two.
4. **Archive Storage**: This is meant for data accessed/ writen to about once a year. This is good for archives and disaster recovery.<br />
Here prior provisioning of a set amount of resource (bounded) is not needed. HTTPS/ TLS security is used and server side encryption is done as well.


## Cloud Storage: Storage Classes

Transfer of data into the storage can be done in several ways:
1. **Using `gsutil`**: Online transfer using the `gsutil` command can be done using the Cloud Shell.
1. **Storage Transfer Service**: To ship data from a different Cloud Provider, a different storage region, etc., this can be used.
1. **Transfer Appliance**: It is a rackable, high-capacity storage server that can be leased from Google Cloud. This appliance can be leased, loaded with data and then used to transfer data to the Cloud Storage. This is better for transfering large amounts of data at once.<br />
Many more ways to ship data exist from within services itself (like exporting tables in BigQuery, using exports from Firestore, etc.).


## Cloud SQL

- They are the solutions to store data from the database directly. They deal with relationsl databases and provide options to launch PostgreSQL, MySQL or SQL Server instances.
- Doesn't require any updates or installations. The instances are equipped with the LTS releases and keep on updating by themselves.
- They can scale appropriately.
- Support automatic repliaction scenarios when load is high.
- Supports managed backups (cost of an instance covers 7 backups).
- Encrypts customer data on VPC networks.
- Includes a network firewall that controls access to any networking to the instances.


## Cloud Spanner

- It is a fully managed relational database service that scales horizontally, is strongly consistent and largely reliable. Google's own database system worth 80 million USD is supported by *Cloud Spanner*.
- It is a solution that can be opted for if the relational database services offered by *Cloud SQL* need to be employed in a large-scale (increased throughput (10000+ reads or writes per second) of data, more than 2 TB of data storage, SQL database with large number of joins and indexes, high-availability).


## Cloud Firestore

- It is a flexible, highly scalable NoSQL database service for mobile and web app development. Features such as strong consistency, atomic batch operations and automatic data replication is there as well.
- The data storage method here is much like MongoDB. Data is stored in Documents (that may contain nested objects or subcollections) that are stored into Collections. 
- The queries used are a bit unique from the general architecture of SQL. Here data is indexed by default. Queries can combine sorting and searching options as well. Multiple, chained filters may be used.
- Data synchronisation for every device is always enabled.
- It uses a cache to store reads, writes where it can listen and query data even if device may be offline. Local changes are synced back to the *Firestore* upon coming online.
- The pricing model of *Firestore* is a bit different. We are charged for amount of data stored, amount of reads, writes and deletes, queries (even if the query doesn't return anything) and network bandwidth used. Ingress and egress are, to some extent, still free.
- Per day, a free quota of *Firestore* has 1 GB of data storage, 50000 document reads, 20000 document writes & deletes. Only if the free daily quota has been expended, charges begin.


## Cloud Bigtable

- It is Google's NoSQL Big Data database service, the very same that powers many of Google's native capabilities of Search, Analytics, Maps & GMail.
- It handles massive workloads giving high throughput at low latencies, making it good for Operational and Analytical operations involving real-time data surveys, IoT, etc.
- Interactions can be done with other serives on Cloud as well.
- Streaming of data can be done as well using Spark, *Dataflow*, etc.
- If streaming is not an option, batch processes can also be run using *Hadoop*, etc.


## How to Choose?

- **Firestore**:
  - **NoSQL**: The project is built on a NoSQL database paradigm.
  - **Scalability**: Massive scaling is supported together with realtime query results.
  - **Web & Mobile Frameworks**: Easy to work with web frameworks since it provisions instances that can be individually connected to. We also have the advantage of mobile apps here.
  - **Medium-Traffic/ Low-Traffic Apps**: The backend of the apps having low to moderate data storage traffic can go for this since this would be easier on costs.
- **Bigtable**:
  - **High Throughput**: Data is rapidly changing and transactions need to be very quick and in huge amounts.
  - **NoSQL**: The project is built on a NoSQL database paradigm.
  - **Big Data**: If data is vast and extensive and needs real-time processing by surveyors, asynchronous batch processing or ML aLgorithms.
  - **ML Algorithms**: If ML algorithms are running on the data entries.
- **Cloud Storage**:
  - **BLOB Storage**: This is practically the only option that should be opted for when storing binary files of any kind that are multimedia (photos, videos, etc).
  - **Files**: Any sort of file can be stored here with a proper heirarchy and policies may be set as to governing the access of the storage, which may be private or public or even more customised.
- **Cloud SQL**:
  - **SQL**: The project is built on SQL paradigm.
  - **Medium-Traffic/ Low-Traffic Apps**: The backend of the apps having low to moderate data storage traffic can go for this since this would be easier on costs and up to 30720 GB of data can be stored. 
  - **Web Frameworks**: Easy to work with web frameworks since it provisions instances that can be individually connected to.
- **Cloud Spanner**:
  - **High Throughput**: Data is rapidly changing and transactions need to be very quick and in huge amounts.
  - **SQL**: The project is built on SQL paradigm.
  - **Larger Storage**: Compared to *Cloud SQL*, it can store Petabytes of data.
  - **Scalability**: The ACID design policies of this database service is built to scale effectively. With *Cloud SQL*, read replicas are used to scale horizontally, or scale vertically by switching device and a minor downtime. The process is much more seamless in *Cloud Spanner*.


## Lab: Cloud Storage and Cloud SQL Introduction

We need to create a VM instance, a Cloud Storage bucket and a MySQL instance. The MySQL instance needs to be connected to the VM instance created by adding its exposed External IP address in the Connections tab of the database.