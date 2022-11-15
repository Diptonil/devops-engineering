# Databases

The solution used to store data of any sort is offered by databases. This should not be confused with file storage mechanisms like AWS S3 buckets or GCP Cloud Storage. Those services are responsible for the storage of media files and binary formats. Here, storage is of textual medium.


## Database Management Systems

The whole reason why database management systems were created in the first place was because that the traditional file storage technique, albeit sufficient and strong enough, was not efficient enough. For a large software application, data becomes abundant and huge, on which the basic operations of CRUD (create, retrieve, update & delete) become harder to facilitate, if all information is stored in file storage. Retrievals become slower, structure of data becomes confusing as well as deciphering relations to data becomes almost impossible. This is why database management systems exist.


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
    - Design Principles of MySQL
1. **Redis**
    - Working with Redis
    - Design Principles of Redis
1. **MongoDB**
    - Design Principles of MongoDB