# Databases

The solution used to store data of any sort is offered by databases. This should not be confused with file storage mechanisms like AWS S3 buckets or GCP Cloud Storage. Those services are responsible for the storage of media files and binary formats. Here, storage is of textual medium. They are more analogous to AWS RDS, GCP Cloud SQL, GCP Firestore, AWS Redshift, GCP Bigtable, etc.


## Database Management Systems

A DBMS is a collection of programs offering an unified interface that is associated with *defining* (specifying the type of data to be housed and their constraints), *constructing* (storing data physically on a database), *manipulating* (altering the data already stored for whatsoever reason), *sharing* (allowing simultaneous access to data by multiple users at the same time) data that is maintained on a database. Other features that a database might offer are *security* (ensuring database is secure with its data) and *long-term maintainability* (ensuring the data can persist and exist in the database for longer time periods).


## Why Database Management Systems Exist?

The whole reason why database management systems were created in the first place was because that the traditional file storage technique, albeit sufficient and strong enough, was not efficient enough. For a large software application, data becomes abundant and huge, on which the basic operations of CRUD (create, retrieve, update & delete) become harder to facilitate, if all information is stored in file storage. Retrievals become slower, structure of data becomes confusing as well as deciphering relations to data becomes almost impossible. This is why database management systems exist.


## Why DBMS is Better Than Regular File Systems?

1. **DBMS are self-describing**: The feature of a DBMS storing metadata so as to put constraints on the type of data to work with is what makes it really great. This makes it less prone to the entry of wrong data by keeping a check on the standards and conditions of data entry. The metadata that is stored in a database is called *system catalog*.
1. **Multiple ways to view data**: Not all users would be interested in everything that a file record has to offer. Some users might want a subset of the data offered by a file system. Normal file-systems don't have that functionality. Writing a query enumerating all that a user needs can, however, show the data in the way they want to see it as.
1. **Multiuser Transaction Processing**: Database can handle concurrent users working on the same data. That is how it is designed. However, file operations don't support such parallel transactions.
1. **Less Redundancy**: File systems often store same information on many different files just to justify that there exists a relation between two data entries. This is greatly simplified in RDBMS using Foreign Keys and in NSQL DBMS using Parent-Child Values.
1. **Access Control**: A DBMS specifies roles to users as to who can do what kind of CRUD operations at any given time. Delegating such access to all file records can be a big hassle.


## Topics

Due to the fact that majority of platforms utilize MySQL, Oracle, DB2, et cetera for SQL (and not PostgreSQL), queries have been dealt completely with MySQL. However, the fundamental RDBMS concepts have been explained with PostgreSQL. Besides that, multiple system design principles of different vendors have been discussed as well.
1. **PostgreSQL**
    - Introduction to RDBMS
    - The Relational Data Model
    - Primer on ER and Schema Diagrams
    - Database Design Techniques
    - Poor Practices in Design
    - Design Principles of PostgreSQL
1. **MySQL**
    - HackerRank & Leetcode Problems
    - Queries for Database Creation
    - Guide on SQL Queries
    - Standard Query Techniques
    - Design Principles of MySQL
1. **Redis**
    - Working with Redis
    - Design Principles of Redis
1. **MongoDB**
    - Design Principles of MongoDB