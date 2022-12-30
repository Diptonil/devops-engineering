# Snakes and Ladders

In this section, the design of the classic game of snakes and ladders is realized. There may be some additional extension and clauses given to the traditional problem. But it is the same at the core.


## Rough Idea About Objects

By default, if every component of the game is made into objects, the rough classes that should exist in game:
- Snakes
- Ladders
- Dice
- Board
- Players
- A Game Session 


## Deciding on the Classes

We note the following factors:
- Snakes and ladders are both items doing the same thing essentially - either promoting or demoting a player to a certain cell on the board. We might as well club their identities.
- We may have *n* dice.
- In cases when the scope of the problem would be extended, we may need special logic particular to each cell in the board. It is better to have a special class for that.


## Final List of Classes

Consult the UML Class Diagram for a better understanding of the relationships. As such, the final list of classes would be:
1. BoardItem:
    - *start*
    - *end*
    - *item*
1. Cell
    - *has_player*
    - *board_item*
1. Board
1. Dice
    - *count*
    - *roll()*
1. Player
    - *id*
    - *name*
    - *current_position*
1. Game