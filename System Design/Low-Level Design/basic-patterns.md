# Basic Patterns

Here we explore the design patterns that we use commonly while creating components of OO code.


## Decoupling

- Decoupling of code refers to the practice of taking a component of code (like a class or a function) and splitting it up into multiple parts so that each component deals with only one issue.
- Decoupling code makes it more readable and maintainable. Functions aren't unnecessarily huge anymore. Every function is small and detailed and is called by some other function. This goes on to display the actual intent of the code pretty well. The function names itself serve to tell what exactly the code does.
- Heavily coupled are too dependent on the whole body of the code. The body, when grows large enough, starts to make less sense.


## SOLID Principles

Introduced by Uncle Bob in his research paper, these techniques roughly state the best methodology to design classes. They have classificications as:


### The Single Responsibility Principle

It states that a class should do one thing and therefore it should have only a single reason to change. To state this principle more technically: Only one potential change (database logic, logging logic, and so on.) in the software’s specification should be able to affect the specification of the class. <br />
For example, refer to `single_responsibility_principle.py`. <br />
**Reasons to Follow It**:
- Multiple teams work in the code simultaneously. If all teams change one single class for multiple reasons, there would be too many merge conflicts and unnecessary issues. A team shall be given complete charge of one simple class. That's it.
- If a class becomes a *data container*, it shall only change if we require some change in the data model. In no other circumstance would it change. Similar to this, all classes would have just one reason to change. This makes it easier to actually define the intent of a class in general. <br />
**How to Implement?**
- Think of precisely what role does the class serve? If a class seems to have multiple responsibilities, we should *decouple* it.
- Start of by keeping classes as minimal as they can possibly be, instead of pouring a lot of things and then try to refactor them into segregation. The former ensures that coupling isn't done by mistake. <br />
**When Does it Break Down?**
- The Singleton Gang of Four design pattern seems to disobey this principle.


### The Open-Close Principle

