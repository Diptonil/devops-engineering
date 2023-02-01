# System Calls

System calls are functions in the OS that processes can invoke using some special instructions. These functions are what the proceses use to interact with the kernel to do operations outside their enclosed scope like read and write to disk, etc. Normally, a process isn't allowed to access anything specific to the OS kernel. It makes that operation possible by this system call, which refers to a particulr call that is definned in a special table (as to what would happen when a call is made). <br />


## Avoiding Context Switches

In most modern OS, the kernel code and the table for system calls are generally placed within the address space of a process. The kernel code lives right above the process' call stack. This is done to avoid context switches. <br />
Whenever a system call is made, the control jumps and executes the kernel code. The system call is placed inside the call stack of functions (in the same way as any other function). This treats the system call as a function of the process itself, rather than wasting resources on switching contexts. This would not be possible if kernel code and the table for system calls weren't in the same address space. <br />
This also gives us the benefit of having natural interrupts to system calls.


## Process Blocking

There are certain conditions in which, in a process lifecycle, we transition a process to a blocked state. This can happen for various reasons. One of them is due to the execution of certain system calls. <br />
For example, a system call made to write to disk can be quite slow for the disk to handle. The process is just blocked off in that case until the write is finished, after which it resumes again (waits for scheduler to put it back in queue).


## Utilities of System Calls

- Processes
- Files
- Networking Sockets
- Signals
- Inter-process Communication
- Terminals
- Threads
- I/O Devices


## A System Call Example

Let us consider the system call for the simple operation of *read*. The UNIX system was written in C, so that would be the starting point of the discussion.
- The C library would, by itself, have certain functions that are necessary for the system calls. The function signature for reading in C:
    ```c
    ssize_t read(int fd, const void *buf, size_t count)
    ```
- The `fd` here refers to the file descriptor (we'll come to that in a bit). The `buf` is the pointer to the buffer. The `count` specifies number of bytes to read. It returns the quantity of data written in bytes.
- Just like we have this for C, we have, in every programming languages (they all somewhat stem for C to be able to have their own semantic wrappers around this very utility), the `read` function that operates in different ways. Due to semantic and structural differences between languages, the return values, inputs, et cetera may differ.
- The Python language equivalent of this is just `read(fd)`. It ultimately uses a wrapper around the C function itself.
- System calls, since they're made in C, have a different mechanism for handling errors (since C has no exception handling feature).
- If any system call function returns the value -1, it is to be understood that the process has been aborted.


## Processes

We already know the abstraction of what processes are. They are the components that make up a process:
- **Address Space**:
    - We have a standard memory structure for a program. They have (from bottom to top): code, initialized data, uninitialized data, heap, stack and kernel code. this whole thing is the address space.
    - The code is the text for the program.
    - The initialized and uninitialized data refer to global variables set aside with or without values in the memory.
    - Heap is the growable or shrinkable space for dynamic memory allocation.
    - Stack is the space that is used to hold function calls.
    - Kernel code is what we had discussed earlier.
- **Process IDs**: Every process is given a unique process ID (generally in the order of them being spawned). When a process terminates, the ID that it vacates can be, however, taken up by another process that gets spawned later.
- **User IDs**: Every process has a user ID that tells the user that owns the process. This also puts the privilege that a process can have under a user so that if there are certain system calls a particular privilege level does not grant access to, the process can never make those calls. 0 is for the root user. System calls never fail for this. It is worth knowing that user IDs are just some numbers rather than being represented by users (in system, although that is how we abstract it as). There are actually 3 IDs that are a part of user IDs:
    - Real ID: The ID of the owner.
    - Effective ID: The ID determining privileges.
    - Saved ID: Set by *exec* to match the effective ID.
- **File Descriptors**:
- **Environment**: It is just a bunch of key-value pairs separated by a line containing information about the user, path to the program, editor used, shell used, etc. It is some kind of configuration data that is passed down from one process to the next by means of forking (as we will see). We can edit environments of a process by using C functions. We don't ever directly do that (it is not recommended).
- **Current & Root Directory**:


## The `mmap` and `munmap` Calls

- To allocate memory in a process, that process must invoke the system call of `mmap` (memory map: used to allocate pages to the process address space) and `munmap` (memory unmap: deallocates memory).
- Consider the pseudocode:
    ```c
    address = mmap(6000)
    ...
    munmap(address)
    ```
- It takes a parameter of how many bytes of memory to assign. The assignment is done internally by the OS. It then gives out the address (handled by the OS) of the first byte of the chunk (it actually might allocate and return more number of bytes since the allocation is done in terms of pages). When the need for the address is over, we unmap it.
- It is an important and overlooker problem to consider the contiguous allocation of memory. The OS may hand out memory from a lot of different areas in the memory. This results in there being small gaps between windows of memory being used. This prevents the OS from servicing a request to hand out a particularly large chunk of memory to the requester. This is why we should always deallocate memory everytime we are done with their use (this especially is noticable in larger programs).
- Modern OSs generally deal with this problem by involving the concept of virtual memory in which allocated memory not in use is actually swapped out with secondary memory to save primary memory for other tasks.
- This is so important in this context because C is not garbage collected. So, there is no mechanism to deallocate automatically when no references exist in memory.


## Forking

The only way in UNIX to create a new process is to make a copy of its own. This process is called forking and is explained in detail in `forks.md`.


## Exec System Call

This too doesn't really create a new process. This just replaces the current program in the process with a new program. This makes the entire address space of the process to get discarded and a new one being created, in turn. Its a completely empty stack with nothing in the heap or the stack. The environment is copied though (with the use of a temporary data store) <br />
What actually happens in a classic scenario in which we decide to start a new process is often - we fork a process first and then in that fork, do an exec system call with the new program in question. This, if observed carefully, takes care of copying a process, swapping the copy of that process with the new program that needs to be run as a process. This also ensures that the process has most of the other components of the parent process like the file descriptors, environments, etc.


## The `init` Process

The question is that if all processes are actually clones of another process - which is the first process? The `init` process (with process ID 1) is the first process from which all others originate. It is like a heirarchial tree.


## When a UNIX System Starts

- The `init` process with user ID 0 (superuser privileges) starts. The process ID is 1.
- Then a `login` process starts next with the same user ID (forked and exec). It has the use to authenticate users.
- The `shell` process with process ID 3 begins. This process has a user ID of whatever user has logged in. This is done using fork, setuid and exec calls.