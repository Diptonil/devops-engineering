# Standard Query Techniques

While writing SQL queries in any engine, there are certain techniques that can optimize query performance as well as enable us to write advanced queries. These can be understood as 'patterns' to ease querying, knowledge of which would let us approach any given querying problem with relative ease.


## Aliasing Tables

Whenever we need to perform a self-join but the attributes of the table, post joining, cannot be distinguished even by using the table name, we need *Table Aiasing*.
- This is a handy concept when dealing with self-joins. 
- We never use the keyword AS here.
- The format is `table_name new_table_name`, during the time of initial aliasing (see example below).
- An aliased table is referred to by the alias at any part of the query (not just after the declaration but also before it).
We need to find out, for example, all employees who earn more than their managers (standard problem). But we conly have the `Employee` table, and nothing else, with the attributes of `id`, `name`, `salary` & `manager_id`:
```sql
SELECT E1.name AS Employee
  FROM Employee E1
  INNER JOIN Employee E2 ON E1.managerId = E2.id
  WHERE E1.salary > E2.salary;
```


## Aliasing Columns

Everytime when the question asks us to give the query output with a certain name for a column, we use *Column Aliasing*. <br />
For example, to show the data in a table with attributes of `fName`, `lName`, `id` as something that provides more context:
```sql
SELECT id AS ssn,
       fName AS first_name,
       lName AS last_name
  FROM Employee;
```