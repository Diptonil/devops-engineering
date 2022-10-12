# The Linux Manual

The Linux Manual (also called as Man Pages) is a user manual embedded by default within each Linux distro. It is for explanation and use of a Linux machine in general. It is divided into sections that elucidate the process of searching for certain commands. We do not need any root privileges or something like that to be able to access it.


## Manual Structure

These are the sections that the manual is broken down into:

1. **User Commands**: Explanation of user commands.
2. **System Calls**: Used for the commands that are incorporated within applications that interact with the low-level Linux kernel.
3. **C Library Functions**: Used for the details of the C programming language libraries and functions.
4. **Devices and Special Files**: Details on how devices (CD drives, ports, etc.), special utilities, random number generators are managed.
5. **File Formats and Conventions**: Details about the use of different types of computer files.
6. **Games**: Details about any sorts of games that might be installed in the system.
7. **Miscelleaneous**: These detail on minor things that do not necessarily fall into any categories.
8. **System Administration**: These detail all the commands that deal with root privileges and overall system administration.

It is worth noting that mostly section 1, 4, 5 and 8 should be needed for DevOps (or most general purpose use).


## Searching for the Man Pages

- The `man` command is used to deal with everything relating to the man pages. The general command structure to search is (the option '-k' is for searching):
```sh
man -k keyWord
```
- It is worth noting that it is not compulsory for the `keyWord` to explicitly be a command. It might be a word that matches with the description in the Man Pages.
- The output follows a form of list that details the occurences of the searched keyword along with the manual section, the respective command and the description.


## Opening the Manual Pages

- Once we are satisfied with the results of the search query, we can look into the manual for the command that we want to look at.
- For example we were searching for the `which` command and our ultimate objective is to gain the man page for it. It would be in the form:
```sh
man -k which
man 1 which
```
- The general format is to type `man sectionNumber commandName`.
- Generally, the search occurs from top of the manual section. So, if a command lies in the 1st section, we may omit the `sectionNumber` input and just go ahead with the command.
- Beyond this information, everything is pretty trivial.


## Drawbacks

- There are certain cases where the command doesn't work in resolving certain issues. On eexample would be that if we searched for the `cd` command using `man`, we would not get anything.
- For all such cases, it is recommended that we use the `help` command.
- The example that gives a valid output:
```sh
help cd
```
