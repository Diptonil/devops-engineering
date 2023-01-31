# Linux

The use of Linux for DevOps is logical since it has all the benefits suited for development and deployment that other OSs aren't particularly geared to handle. Modern servers are mainly reliant on the distros provided by Linux. <br />
A *distribution* (distro) is a variation of an OS that has the Linux kernel as well as GNU tools, other softwares and a package manager. Every distro has the kernel core common. These can either be commercial or free. The distro most widely opted for in this field is Ubuntu.<br />
For in-depth exploration of the basic commands, it is highly recommended to check out the manual pages for the same command. Practicing things in the terminal instead of the GUI is a sure way to gain proficiency rather than learning up commands and never getting back to it after one complete session of learning.


## Running Ubuntu

There are multiple ways to learn Linux. However, out of these, sum are not wholly recommended for development. Most can be used fine for learning. They are:
- **Ubuntu OS**: Running the OS on the machine bare metal is the choice best suited for developers. Dual boot systems can also favour this. Not necessarily recommended for learning just because some cases of experimentation may have unexpected results.
- **Ubuntu on a Virtual Machine**: Use a VM service like VirtualBox or VMWare. Use the Ubuntu disk image. This is particularly advantageous for learning since it is a sandbox in which experimentations can be done. It is also beneficial as a small-scale app testing environment.
- **Windows Subsystem for Linux**: It is used to run Linux in conjunction with Windows. So it has the best of both the worlds and oftens provides features that might also seem better than the regular OS. To continue Linux without losing the convenience of Windows, use this.
- **Ubuntu Docker Image**: This options allows minimal playtesting with Linux commands for familiarizing oneself to work on such an environment. It is easy to experiment even more dangerous things here since containers can just be thrown out anytime and the process of spinning another one up is faster than a VM.


## Why Linux?

- We can tailor a Linux machine to suit our server needs, unlike Windows.
- Known for reliability and stability. Many Linux servers on the Internet have been running for years without failure or even being restarted.
- Maintenance & ownership costs are less than the competitors OSs.
- Extremely secure.
- It is free and open-source. Servers of major Cloud vendors leverage this to cut costs.
- Developer friendly.


## Contents

The markdown files here detail every part of Linux covered here:

- Operating System Theory
    - Shared Memory
    - Free Memory
    - Available Memory
    - Virtual Memory
    - Swap Space
    - Kernel
    - Daemon
    - Redundant Array of Inexpensive/ Independent Disks
    - Principle of Least Privilege
    - Power On Self test
    - BIOS
    - Processes
    - Threads
    - Synchronous Operations
    - Asynchronous Operations
    - Multithreaded Operations
    - Multiprocessing Operations
    - Inter-Process Communication
    - Mutex
    - Semaphores
    - Interrupts
    - Context Switches
    - Forks
- Linux Terminal
    - Introduction
    - Specific Commands
    - Redirection
    - Pipelining
- Linux Manual
- Linux Commands
    - Commands
    - Aliases
- - Linux Performance Commands
- Linux Environment Variables
- Linux File System
    - File Extensions
    - Wildcards
    - Searching Files
    - Creating Files
    - Permissions
    - Archiving
    - Compression
- Linux Software Ecosystem
- Linux Special Files
    - The `.profile` file.
- Bash