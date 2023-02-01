# Important System Calls

Here, important system calls are described and elaborated upon.


## `_exit`

- A process can be terminated for a multitude of reasons. If a process chooses to terminate itself, however, it does so using the `_exit(0)` system call. There are many similar system calls with minute differences.
- There already is an `exit` function in C library, so we have an underscore to distinguish between the two.
- It takes an exit *code* as a parameter. It indicates teh cause for termination. 0 means the program was over and hence the process terminated itself (natural exit).
- Some programs make use of their own codes to indicate errors (which can be gauged by their documentations).


## `wait`

- When a process exits (as shown above), it has to return its exit code to its parent process.
- For this, a parent process has to wait using the `wait` system call that takes in the *process ID* as an argument. this makes the parent wait until the child is done executing and exits by calling the `_exit` call.
- Since the parent process now has the exit code of the child process, it can make a bunch of decisions henceforth. It basically knows if the child process finished off succesfully, or there was some error (if yes; the kind of error).


## `setuid`


## `seteuid`