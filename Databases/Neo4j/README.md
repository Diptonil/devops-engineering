# Neo4j

Neo4j is an open-source graph database that uses the property graph data model, instead of the relational data model that RDBMSs do. It comes with different language drivers for support with regular programming. It uses the Cypher Query Language to process data (like SQL for RDBMS). It can perform native graph processing as well and is *one of the most established graph database service*.


## Graph Databases

- Data here is represented as nodes that may have links and relationships to other nodes.
- Each node represents a tuple of data.
- Nodes contain data in form of key-value pairs of properties (attributes or columns in RDBMS) and their corresponding values.
- Nodes are classed to belong to a particular entity type (like tables in RDBMS) using labels.
- Relationships may exist among any type of nodes in as many numbers. Relationships are always unidirectional and may have a set of associated properties.


## Why Choose Graph Database Over Others?

- Graphs can be good in situations where there is a greater focus on complex relationships between the data across different entity types.
- Relational Data Model may not suffice in representing intra-entity type relations. That can easily be handled by graphs by applying realtions across nodes.
- Recommendation Engines might be implemented with greater ease in Graph Databases with filtering techniques.
- More alterations to an RDBMS tends to degrade its performance and makes it unmaintainable, unless the handler is trained well enough. This may lead to messing up of realtions very easily. Graph databases have lesser troubles with maintainability.
- Complex queries in RDBMS require multiple joins across different tables, which gets unnecessarily tedious with the increase in data and relations. Graphs handle it extremely well, no matter the increase in relations or nodes.


## Native Graph Technology

- Two main elements distinguish native graph technology: **storage** and **processing**.
- **Graph Storage** is the underlying mechanism that is responsible for the storage of data in graph format.
    - **Native Graph Storage** happens when the data is effectively stored in the graph database because the data was structured in a way apt for being stored in graphs. This leads to effective handling of data in graphs.
    - **Non-Native Graph Storage** happens when data is coerced in graphs as nodes even when it actually was meant for column-wide or other NoSQL databases. This leads to non-effective data handling in graphs.
- **Graph Processing** is the underlying mechanism that is responsible for the processing of data in graph format.
    - **Native Graph Processing** is an important tenet that makes graphs faster. It lets retrieval occur at lightning speeds without any reliance of indexes. This is because data is stored directly into nodes and the whole structure was graphical to begin with.
    - **Native Graph Processing** happens when Non-Native approach is employed. A lot of indexes need to be deployed here to achieve speed since data originally wasn't graphically modelled. This makes the database bulky and adds complexity, thus slowing down operations.


## Graph Data Model

Graph data modeling is the process in which a user describes an arbitrary domain as a connected graph of nodes and relationships with properties and labels. Like we have the Relational Data Model for RDBMS, we have a Graph Data Model.
- It looks like a rough graph with nodes representing the data items and the edges representing relation between nodes.
- Data is easily represented in this way using whiteboards as well. As always, this model is relation-forward. So the more intense the model of relations are, the better it is.
- A Property Graph Diagram is used to graph the whole model of any designed database to represent it.


## Connecting to a Database

We have many options available. A valid way is to make use of a Docker container from the official image. We can also use the provisioned service by AuraDB that makes things easier and lets us have a database instance in the cloud. We can have one free instance forever and the instance should be useful for a lot of purposes with no notable restrictions.


## Schema and Constraints

In Neo4j, the definition of a schema is optional (which makes it easy to work with lots of data quickly without being too ceremonious). We define a schema in big projects if we find it appropriate that we have some sort of data integrity. <br />


## Indexes

- We might also create indexes for fast lookup of nodes and subsequent relations.
- We have talked about Neo4j being a native graph. This means that indexes are irrelevant for its speed. It is important to know that traversals in graphs don't require indexes. Indexes are essentail just to find the *starting point of retrieval of data and lookup*.
- Relational databases work different in cases of indexes. No matter what, after a certain point, even if we do have indexes, the database performance takes a severe hit in cases of joins.
- The operations benefitting from the use of indexes are:
    - STARTS WITH
    - Equality
    - CONTAINS
    - ENDS WITH
    - Range searches
    - Non-existent checks


## Cypher

This is the querying language generally used for making queries to the database. An example that returns the node that to the film "Matrix" along with the number of reviews it has would be:
```sql
MATCH (m:Movie {title: 'Matrix'}) <-[:RATED]- (u:User)
WITH m.title AS movie, COUNT(*) AS reviews
RETURN movie, reviews
ORDER BY reviews DESC
LIMIT 5;
```

The documentation provides a fairly extensive discussion on the queries that can be made. So further discussion on it would not be done. 
