# Linux Performance Commands

The commands here discuss more about the performance commands in the Linux ecosystem along with their options.


## The `vmstat` Command

- It is also known as virtual memory statistic reporter.
- It is used for performance monitoring as it gives the information about processes, memory, paging, block IO, disk, and CPU scheduling. 
- It takes in, along with options, *delay* (how many seconds to wait before automatically running the command) and *count* (how many times to automatically run the command).
- Good to use in scripts to monitor memory or other stats periodically.
- The memory section details with the system's main memory. The info displayed:
    - Free space.
    - Buffer memory.
    - Cache memory.
- The swap section tells about the memory that gets swapped in (`si`) and out (`so`) of disk in kBs.
- The io section tells about the kBs recieved from a block device (`bi`) and sent to a block device (`bo`).
- The system section tells us about the interrupts and context switches.
    - `in`: Interrupts
    - `cs`: Context Switches
- The CPU section details the percentages for CPU time.
    - `id`: Time spent idle.
    - `sy`: Time spent running kernel mode.
    - `us`: Time spent running non-kernel mode.
    - `st`: Time stolen from a virtual machine.
- The options we mostly use:
    - `-a`: Display active and inactive memory.
    - `-f`: The number of forks since boot.
    - `-s`: The best option to pair the command up with. display the statistics of the system in a verbose way where everything is understandable.
    - `-d`: Disk statistics.
    - `-t`: To show the timestamp when delay and count are also given to run with this command.


## The `free` Command

- Used exclusively to gain insights on memory.
- In the `Mem` sections, we have:
    - The total memory.
    - The free memory.
    - The used memory.
    - Shared memory.
    - Memory used by kernel buffers.
    - The available memory.
- Options:
    - `-m`: Show in mB.
    - `-g`: Show in gB.


## The `fdisk` Command

- Also known as the format disk command. It is used to create and manipulate the disk partition table.
- It can be used to create space for new partitions, organize space of new and old drives, copy and move data across the partitions.
- Options:
    - `-l`: Basic details about all available partition.


## The `top` Command

- All processes and their corresponding info are shown. The first part shows the system stats and resource usage. The second part shows the list of all processes running.
- We can see:
    - The process id.
    - The user that started the process.
    - The priority level of the process.
    - The CPU and memory usage percentage.
    - The virtual memory being used.
    - The shared memory being used.
    - Physical RAM that is being used.
    - The command that was executed to start the process.
- The command keeps on executing until we break out of it. It is an automatic monitoring process.
- Options:
    - `-n`: The monitoring process exits when a certain count of repititions are achieved.
    - `-d`: To set repitition delay time.
    - `-s`: Use top in secure mode.