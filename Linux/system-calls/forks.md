# Forks

It means copying itself. When the copy is being made, each and everything about that process being forked is copied (address space, file descriptors, etc). <br />
When forking is done, the parent process that actually invokes the fork gets the child ID of a process returned to it. The child process that gets forked, however, is returned a 0 for a succesful fork. <br />
This means if 0 is returned, we know that we are inside the child process. Otherwise, we are actually inside the parent process.


## How Expensive Are Forks?

If a process if being completely copied, it might be quite expensive. But that is not actually the case in the newer UNIX systems (used to happen like that in older systems). <br />
Here, virtual memory is used for aiding the process. The *memory tables* are copied, not the actual content of it.


## What Actually Happens in the Modern Implementation?

- When a fork is done, a child process is actually mapped to the very same location of address space as its parents in the memory. They share the same storage whether in RAM or hard drive (by pages).
- As such, whenever any process reads, the functionality can still be smooth since it doesn't alter the memory. With a read, both still point at the same location in memory.
- However, the moment a write operation is to be done, there is an exception that gets triggered in the CPU. This makes the OS copy all the pages and update the fork (table).
- In reality, every fork of a process actually results in a very few pages of the memory getting copied (kBs) throughout its lifetime.