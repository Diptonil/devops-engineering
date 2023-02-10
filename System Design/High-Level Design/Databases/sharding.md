# Sharding

Sharding is quite a complex concept to engineer correctly, which is why we delegate this to execute when all the other design techniques up our sleeves are exhausted. So, this must be treated as a last resort for databases.


## Concept

Sharding is the idea of taking a horizontal partition (or the like) of an overgrown table and putting it in a whole new instance altogether. As a hypothetical example, we have a table with primary keys of 1 to 32 in instance one and from 33 to 64 in instance two. <br />
The two segregations that are made are called *shards*.


## Consequences

- We cannot allow transaction operations such as rollbacks or commits.
- ACID doesn't hold here.
- The whole logic about looking through the sharding ID (the identifier that decides which instance to go to for a query) is built into the client application, which is hard to execute. This leads to coupling in which a component (client application) is aware of another component (database), which leads to the violation of separation of concerns.


## Resharding

This is a concept where it is best to *not* venture into, because it calls for a refactor to the range that has been selected for sharding. It is complex to do. <br />
For such things, we have a middleware that we can lay atop our applications called **Vitess** (open-sourced). It does all the heavy-lifting for us.