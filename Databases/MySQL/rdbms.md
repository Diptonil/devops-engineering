# Relational Database Management Systems

RDBMS are a class of systems that provide an interface to store data in a format that is heavily influenced by *relations*. The primary tenet of such a system is that the data is completely based on their relations among one another. This lets us define the structure of the way data is going to be stored more comprehensively so that things are clear. This also allows us to set up certain preordained restrictions that act as constraints on the data that is about to be entered. This provides a cohesive and secure interface for operations on data.


## Basic Terminologies

1. **CRUD**: Create, Retrieve, Update & Delete.
1. **Data Model**: A collection of concepts used to describe the structure of a database.
1. **Database Schema**: Rough description of a database with all it's tables and columns that is not expected to change too often.
1. **Schema Construct**: Database tables.
1. **Relations**: Database tables.
1. **Attributes**: Columns of a table.
1. **Tuples**: Rows of a table.
1. **Transaction**: The execution of a certain instruction or a process on one or more database that involves doing a CRUD operation on it. The ACID theory sheds more light on its use in databases.
1. **Snapshot**: The data in the database at a given time is database state or snapshot.
1. **Metadata**: Descriptions of the schema constructs and constraints stored in *system catalog*.


## Database Languages

1. **Data Definition Language**: The language used to define the framework of the structure of data and set restrictions on it is known as DDL. Example: CREATE, ALTER, DROP, TRUNCATE, etc.
1. **Data Manipulation Language**: The language used to perform CUD operations on the data is DML. Example: INSERT INTO, DELETE, UPDATE, etc.
1. **Data Query Language**: The language used exclusively for all retrieval operations is DQL. Example: SELECT.
1. **Data Control Language**: The language that mainly deal with the rights, permissions, and other controls of the database system is DCL. Example: GRANT, REVOKE.
1. **Transaction Control Language**: This language is responsible for dealing with database transactions. Example: COMMIT, ROLLBACK, etc.