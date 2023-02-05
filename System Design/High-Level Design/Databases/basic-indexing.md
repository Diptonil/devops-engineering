# Indexing

- Indexing is a technique used in databases to finally lead to faster queries, which is quite important in production environment. 
- An *index* is a data structure laid atop a table that acts a lot like the real-life example of a phone-book that has markings that are visible from outside the book - A, B, C..., thus allowing retrieval queries to be sped up by referring to a particular index during lookup and continuing down that index, rather than parsing through all the available records.
- It internally uses B-trees or LSM trees as their data structures. It allows us to search effectively, basically.


## Querying an Index From an Indexed Lookup

- Consider an `employee` table having `id` (the primary key) and `name` as attributes. We run this query:
    ```sql
    EXPLAIN ANALYZE SELECT id FROM employee WHERE id = 2000;
    ```
- The `EXPLAIN ANALYZE` (in PostgreSQL) helps to fetch the time a query requires to be processed, along with other background details.
- It is obvious that there exists an index on the `id` attribute (because the primary key by default always has indexes attached to them).
- Once we run the query, we notice that we have some fields:
    - **Index Only Scan**  means the retrieval operation was done on the database using the table indexes.
    - **Heap Fetches** here is 0. This means that the data that was queried did not have to come from heap. This is because here the data directly came from the index (since we are only retrieving `id`s). This is called an **inline query**.
    - **Planning Time** refers to the time taken by the engine to decide on the best possible way to execute the query.
    - **Execution Time** refers to the time spent by the engine in actually executing the operation.


## Querying a Non-Index From an Indexed Lookup

- Consider an `employee` table having `id` (the primary key) and `name` as attributes. We run this query:
    ```sql
    EXPLAIN ANALYZE SELECT name FROM employee WHERE id = 3000;
    ```
- Here we get a planning time similar to what we had got the previous time. But the execution time is a lot more compared to the previous case.
- This is because even though it is being found in the index data structure (the id that is being matched), the retrieval of `name`s is being done from the table of the database, which is a read from the pages of the disk. It is a heavier operation, undoubtedly.


## Querying From a Non-Indexed Lookup

- Consider an `employee` table having `id` (the primary key) and `name` as attributes. We run this query:
    ```sql
    EXPLAIN ANALYZE SELECT id FROM employee WHERE name = 'Dorian Gray';
    ```
- There is no index of the `name` column and hence the table resorts to a sequential one-by-one search that is the **full-table scan**. This is the condition that must be avoided in databases as much as possible.
- Here, it doesn't matter that the item that is being fetched is actually itself having an index.
- If we execute the statement below and create an index on `name`, we would get a blazingly fast query.


## Creating an Index

- Consider an `employee` table having `id` (the primary key) and `name` as attributes. We run this query:
    ```sql
    CREATE INDEX name_index ON employee(name);
    ```
- As obvious, we are trying to create an index on the `name` attribute of the table.
- Since a data structure spanning quite a bit of memory is being created, it would take some time.


## Matching an Expression Instead of a Value

- Consider an `employee` table having `id` (the primary key) and `name` as attributes. We run this query:
    ```sql
    EXPLAIN ANALYZE SELECT id FROM employee WHERE name LIKE '%Gr%';
    ```
- Here both the columns are indexes (assume).
- It is important to understand the implications of an expression and a value on an index. The LIKE clause craetes and gives an expression. There is no other choice but to resort to a full-table scan despite the index being present because the absolute value is not searrhced through, parts of it are. The index is in no position to handle that. It was not made for it.


## Cons of Indexes

