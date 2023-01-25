# Recommendations Using Neo4j

Building a recommendation engine is a huge part of the extensive use-cases Neo4j has to offer. Generally, when we look at such mechanisms, we can go for 2 types of filtering (extremes). Most real systems are somewhat of a hybrid between the two. All are somewhat reliant on the theory of *Triad Closures*.<br />
A very important thing to understand that recommendations are ideally realtime. We cannot have an item that enters that database and simultaneously gets mapped to existing values because:
- Users' preferences are not considered.
- New values entering wouldn't get considered by the old items' recommendation.


## Collaborative Filtering

- This algorithm considers users' interaction with the products with the assumption that other users would behave in similar ways.
- Play Store has a section called 'Users also installed' that works on this principle. It assumes that just because someone else also does something, the others who are using such a product or service would have same taste and would be open to subscribing to the similar recommendation.
- For example, Will and Amelia both play the game Plants Vs. Zombies. Amelia has also played the game Hitman.
    - Based on just this information, we can draw a conclusion that Will should also play Hitman just due to that factor of interest.
    - The con to that is that the games have nothing in common and the match-up here is purely coincidental because there is no game genre similarity here.


## Content-Based Filtering

- Algorithm that considers similarities between products and and the categories of products services.
- This considers each individual item (data item) and extracts some information or metadata about its particulars to gather similar information and class them into one. THis is how groups are formed so that any item chosen from a group would lead to other items of that group being recommended.
- For example, Will and Amelia both play the game Plants Vs. Zombies. The game belongs to the genre of Tower Defense (which is assumed to be a node having a relationship with the game). We also have the node named Kingdom Rush (one of the best tower defense games) mapping to the genre.
    - Based on just this information, we can draw a conclusion that if Amelia comes to play Kingdom Rush, she should be recommended Plants Vs. Zombies.
    - The con to that is that despite the genre being the same both the games, there might not be any players who actively play Kingdom Rush. So, there is a chance that despite similarity in genre, the games are actually quite different to the users' tastes.
- Here, we can also recommend on the basis of a heirarchy. For example, we can also recommend something that does not just belong to the genre of Tower Defence directly. If Tower Defence is a sub-genre branching out from a direct genre of Casual, any game that has a genre as Casual may also be recommended for a Tower Defence game.


## Triad Closures

In Graph Theory, *triad closures* mean instances when a unidirectional graph has 2 nodes pointing to the same node. If that happens, there is an automatically inferred relationship between the 3rd node. If closely observed, this is what is indirectly used in all the recommendation systems.


## Cons of Data Lakes for Recommendations

When we are to implement a large-scale version of an extensive recommendation system, we have data spread out across a lot of databases. We may have:
- **Document Databases** for product catalogues.
- **SQL Databases** for purchase records.
- **In-Memory Key-Value Stores** for shopping carts.
- **Search engines** for search functionalities.
Amidst all of these, we can easily take all the data from these places and put them into a data lake. That is where we can run analytics, BI, etc. However, there are cons of this since there is a significant transactional speed that needs to be kept in the mind to process recommendation queries for all users. This is expensive. <br />
This is where Neo4j shines. It can remove the use of a data lake and bring something more realtime and faster. Plus it is easy to implement.


## Steps to Design Recommendations?

Before building the system, we need to know the end-goals, design policies and the requirements for which we are building this service. We must be clear regarding these questions:
- What recommendations are we making? What exactly?
- List out all the types of recommendations we are making.