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
