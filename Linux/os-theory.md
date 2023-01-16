# Operating System Theory

Here, we discuss the important concepts behind an Operating System's functioning.


## Interrupts

## Context Switches


## Redundant Array of Inexpensive/ Independent Disks (RAID)

- We build our storage with redundancy (duplication of critical functions), so that one part of failure in the disk doesn't bring down the whole system. Reads and writes are spread out over more than a disk. Our data exists in more than one place.
- RAID is not backup. A backup is a failsafe when a system is corrupted. However, here, if a system gets corrupted, the mirrored RAID gives us two copies of corrupted systems. RAID works with replication, which may be by mirroring or parity.
- We have levels in RAID, which aren't representative of the disks that are being used.
    - **RAID 0**
        - It has 0 redundancy.
        - Data is **written across the drives** (data is *striped*).
        -Data can potentially be read from more than one drive concurrently. This is a major performance boost. That's all it is useful for; not long-term data storage.
    - **RAID 1**
        - It has redundancy.
        - Data written to a drive is *mirrored* to its paired drive. Every drive exists with a pair to be written to.
        - Everytime data is written to a RAID1 device, it goes to both drives. This is why write performance is slower, but reads are faster.
    - **RAID 10**
        - Both RAID1 and RAID 0 are combined.
        - We create a RAID 10 device with 4 disks: 1 pair for RAID 0 & 1 for RAID 1.
        - RAID 1's redundancy + RAID 0's performance.
    - **RAID 5**
        - Works on the principle of parity data.
        - Needs at least 3 equal size disks drives to function. They must be identical for this to work. Complete copies of data aren't stored in the drives. They're broken into parity data to be stored.
        - If one data drive dies, *system can be rebuilt with no data loss*. If more drives die, we have to resort to backup. This is a nice feature.
    - **RAID 6**
        - Similar to RAID 5, but sets aside 2 parity disks.
        - This means, it can recover from 2 failed disk drives.


## Power On Self Test

- This is a set of routines that are to be executed by the firmware after the computer is powered on to determine if the hardware is working as expected. If not, BIOS issues an error message.
- When power button is pressed, it sends power to the boot-loader in the cache memory. The Boot loader performs POST as a preboot sequence. If everything is working well without any errors the BIOS (Basic Input Output System) is activated which finds and loads the operating system.
- The principal duties of the BIOS during POST are:
    - Find, size, and verify the system main memory.
    - Initialize BIOS.
    - Identify, organize, and select which devices are available for booting.
    - Verify CPU registers.
    - Verify the integrity of the BIOS code itself.
    - Verify some basic components like DMA, timer, interrupt controller.
    - Pass control to other specialized extensions BIOS (if installed).
- The POST does a lot of things - **loading the kernel is not one of those**.
- Fundamentally, it has everything to do with the BIOS, checking of hardware health, registers, etc.
- Checks are performed majorly on hardware, keyboard, other peripheral devices, CPU registers, timer, interrupt controller, DMA, etc.
- Errors commonly are:
    - Unstable processors.
    - Incompatible RAM types.
    - No good banks.
    - No detectable RAM.
    - No good boot images.


## Basic Input/Output System (BIOS)


## Threads




## Synchronous Operations

- There can be multiple types of operations happening in a machine. They can be related to a particular service or software running, or a lightweight or a heavyweight system operation going on.
- Synchronosity means pre-ordainment and a predefined lifecycle that is strictly bound. It means that one task has to be done after another, and another. That particular route has to be followed compulsorily. A process might be waiting for the disk to read and send it data, but while the disk does its operation, all it can do is wait. Nothing else.
- Hence, when a process is synchronous, it is tightly bound and cannot do any other work unless the process completes. Hence, CPU cycles are wasted with the process thread doing literally nothing.
- There is only one thread in a process doing all the work.
- This is the default behaviour of most old hardware. These days, a lot of optimizations can be done within a process to make optimum use of CPU.


## Asynchronous Operations

- The thread in synchronous systems that was properly scheduled to adhere to flow of process sends a request to the system stating that it would go on and do some other work while the process executes and is handed off to some resource (like a disk for reading, a printer to literally print, etc.). Once that operation by the device is done, a function call should happen that would bring the thread back. So, to bring the thread back, there are always *callback functions*.
- They are always single-threaded.
- One of the most elegant systems implementing this example is NojeJS - which is a single-threaded, non-blocking asynchronous framework.
- The largest disadvantage of this method is that there are way too many callbacks that need to be designed for every task that the thread may branch off to do. Coding that would be ugly as well.
- A fix was implemented by introducing async and await concepts. That made code that was asynchronous look synchronous with a bit of a syntactical sugar.


## Multithreaded Operations

- A thread is a lightweight process that lives within a space having access to all system resources, codes and files. It originates from a place known as the thread-pool from where, upon demand, threads can be spun up and used to do concurrent work.
- This means, there are many threads in a process to do a task. Obviously, we have speed gains here.
- We need to, however, take care of concurrency issues that may arise due to all threads having access to the same low-level system resources and files. We might run into situations where a certain element of a resource in the system is being attempted to be altered by two or more threads. That is risky.
- Thread safety is the state of a system where it runs no risk of having problems with respect to thread concurrency or many threads trying to alter the same resource. While this is possible in theory, programming such a situation where thread saftely is guaranteed 100% of the time is not easy and is not always possible. This is why many engineers dislike multithreaded systems since its problems outweight the potential advantage it offers.
- We have many mechanisms like mutex locks, etc. to ensure thread safety, which would be explored later.


## Multiprocessing Operations

- Instead of dealing with all the mess of making a thread asynchronous or having multiple threads in the first place, here we have everything as a well-defined, singular process.
- Each huge process, to speed it up, executes as multiple processes. they communicate via *inter-process communication*.
- The best thing about such a process is that a process can be made into a multi-process architecture and, to speed up to the extreme limits, can even be scaled across different systems.