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
