# SQL Query Practice

This section will contain the solutions to all the SQL problems that are given in Hackerrank (or Leetcode, sometimes). The solutions are solved using the MySQL Engine but fundamentally, no advanced functions only particular to MySQL are used that would be incompatible with PostgreSQL. <br />
Some queries that might otherwise by complicated would be discussed here.


## SQL Query Conventions

- Always use singular nouns for column and table names. Column names may have words separated by '_'s (still, the less the merrier). We may use letters and numbers to construct a name (that is as short as possible) PascalCase might be used as well but it generally depends on the users. 
- Since ideally a table has only one primary key column, it may be conventionally wise to just leave the name as `id` and reference that particular field as `table_name.id` instead of `id` (useful in case of multiple tables). Names like `table_name_id` have also been prevalent.
- Column names shouldn't be SQL keywords.


## Keywords

- **SELECT**: Basic statement for signalling retrieval. Anything that shall be processed is written next to it. For example, columns that would be fetched, results of functions that operate on the columns, etc.
- **FROM**: Signals the prepended statement from where the data that is needed would come from. For example, a table.
- **DISTINCT**: Appended before a column (generally in conjunction to SELECT) so that only distnct values from the rows are picked. For example:
```sql
DISTINCT names
```
For a column names, if it contains more than one entries for a particular name (say Arnold), only the first entry would be accepted while the rest of the *rows* would be negated.
- **ORDER BY**: It is used to sort row data in the mentioned columns.
    - The default behaviour is set to sorting in ascending order.
    - `ORDER BY col1, col2` *does not* mean `ORDER BY col2, col1`. The first means that we display data where `col1` is sorted in ascending order and in case we have similar data rank while sorting (there occur, for example, 2 rows having a value of 70), the conflict is resolved by sorting the data on the basis of ascending order of `col2`. The same, if applied to the second statement, would give us different meanings.
    - Do not use `AND`s or `OR`s here. A simple comma is sufficient.
    - Explicitly mentioning the `ASC` or `DESC` might be preferable for users who are not too experienced in managing or working with databases.
- **OFFSET**: It is used to skip a given number of records (rows). Always used in conjunction to ORDER BYs.
    - Can be used in conjunction with FETCH. However, the same functionality may be obtained with a LIMIT clause as well. The syntax transforms into: `LIMIT 1 OFFSET 3`. We don't need to mention ROWS or anything else as such.
    - This example skips over the first row of the ordered result:
    ```sql
    SELECT name
    FROM Employee
    ORDER BY Salary
    OFFSET 1 ROWS;
    ```
- **LIKE**: It is a clause that can be added in conjunction to WHERE to filter out data by matching patterns. A code snippet is:
    - We note that the use of multiple conditions require ANDs or ORs and not commas.
    - The first example matches elements starting with A and ending with 'x'.
    - The second example matches elements that contain the word 'twee'.
    - The third example matches elements having the second character as 'h'.
    - We cannot completely use any forms of Regex by applying '[]' instead of using ORs just to cut short the code.
    - We may use NOT to alter the boolean conditions of an expression (`NOT LIKE...`). Cre must be taken of any ANDs or ORs, if lying around. Sometimes queries don't work as expected just because ANDs or ORs alter the logic and we do not pay attention.
    ```sql
    WHERE col1 LIKE 'A%x' AND
        col2 LIKE '%twee%' AND 
        col3 LIKE '_h%';
    ```
- **AS**: Basically used to alias something or to refer to something.
    - We can use `SELECT col1 AS name, col2 AS age` to change the column names when the result is displayed.
    - We can use it in conjunction with complex functions to make references. For example: `CAST(col1 AS INT(2))`.
- **JOIN**: Refer to the discussion.


## Joins

- A JOIN clause is used to combine rows from two or more tables, based on a related column between them.
- An **inner join** displays the records that have matching values in both tables.
    - Assume we have two tables - Order and Customer.
    - The syntax:
    ```sql
    SELECT Order.OrderID, Customer.CustomerName, Order.OrderDate
    FROM Order
    INNER JOIN Customer ON Order.CustomerID=Customer.CustomerID;
    ```


## Standard SQL Functions

- **COUNT()**: Takes the parameterized column and returns the number of rows it has.
    - It can be used standalone and not with general queries, we cannot query a table and expect it to give us all the rows in a column as well as a single entry of the row count.
    - It is different from the LENGTH() function.
    - It operates on a given column, not its individual row elements.
    - This type of value is called an *aggregation*.
- **LENGTH()**: Takes the parameterized column and returns a column of the number of characters every row has.
    - It can be used with general queries of other columns.
    - Should not be confused with the COUNT() function. Both are extremely different.
    - It operates on individual row elements.
- **LEFT()**: Takes a column name and a number as parameter. Extracts and returns a string containing the parameterised number of characters, taken from the left of the element of the column. Useful for conditional checks.
- **RIGHT()**: Takes a column name and a number as parameter. Extracts and returns a string containing the parameterised number of characters, taken from the right of the element of the column. Useful for conditional checks.
- **CAST()**: Takes an expression in form `column AS DATATYPE(parameters...)` and given the result. Can be applied to all items in a column individually (basically like the LENGTH() function).
- **DECIMAL()**: Takes two parameters - total width and number of digits allowed to appear after the decimal point. Can be used without the function form as well when creating tables.
- **INT()**: Takes a parameter of total width. If the number stored has a larger width, the entire number is shown, not a number trucated to the parameterized digits. Can be used without the function form as well when creating tables.
- **MAX()**: Takes a column name as a parameter and returns a single value - the maximum value (like the COUNT() function).
- **MIN()**: Takes a column name as a parameter and returns a single value - the minimum value (like the COUNT() function).
- **SUM()**: Takes a column name as a parameter and returns a single value - the sum of all rows in the column (like the COUNT() function).
- **AVG()**: Takes a column name as a parameter and returns a single value - the average of all rows in the column (like the COUNT() function).
- **CEIL()**: Takes in a column name and returns a column of elements rounded off to next integer.
- **FLOOR()**: Takes in a column name and returns a column of elements rounded off to previous integer.
- **ROUND()**: Takes in a column name and returns a column of elements rounded off values.
- **POWER()**: Takes in a column name and the power to raise all its values to.