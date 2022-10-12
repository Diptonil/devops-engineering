# Software Management in Linux

Linux was released under the GPL as a Free Software. Obviously, open-source plays a vital role in the existence of Linux and its popularity. <br />
The official <a href="https://www.gnu.org/software/software.html">GNU Software</a> website has a list of all softwares that can be used on a Linux machine.


## Software Repositories

- They are libraries of different softwares that we can install, update and use. They make it easy to work with softare all the while maintaining security.
- There are 4 main repositories at Ubuntu:
    1. Main: Free, open-source softwares maintained by the Ubuntu people (Canonical).
    1. **Universe**: Free, open-source softwares maintained by online communities.
    1. **Restricted**: Proprietary device drivers.
    1. **Multiverse**: Restricted softwares.
- In the 'All Packages' section of the ubuntu website, we can see in the square brackets the type of repository. 
- Packages may have dependencies stacked on top of each other (somehat like Docker image layers).
- For downloads, it is best to run `uname -m` and check out the computer architecture since downloads differ for different architectures.


## Package Managers

- Much like package managers of different programming languages, they are responsible for providing proper installation of packages and their dependencies, ensuring correct version numbers as well.
- The Advanced Package Tool (`apt`) is also a command that provides package management utilities for Debian-based systems.
- The `apt-cache` command is used to deal with `apt` in its cached mode. This means results would come from the cache (it can be read about even if not connected to the internet). Obviously, this also means stale results. It is located in `/var/lib/apt/lists`.
- The `apt-cache search command` is used to search up the command from the software repository's cached results.
- The `apt-cache show command` is used to show detailed information about the command from the software repository's cached results.
- In order for a cache to be useful for anything else other than basic information retrieval, the files should be up to date as they are on the server.


## Updating & Upgrading Cache

- For things to work properly, long story short, as stated above, we must have the cache updated.
- The command `sudo apt-get update` does the work. This needs administrative privileges (`sudo...`) because important files on the system's apt-cache would get swapped with their newer versions. This command updates the cache as to the changed versions of the softwares. However, it doesn't install all of those quite yet.
- The command `sudo apt-get upgrade` is actually used for the upgradation.


## Installing & Uninstalling Softwares

- The command `sudo apt-get install package` is beneficial for the installing process.
- Always update before installing.
- The command `sudo apt-get remove package` is beneficial for the uninstalling process. It should be noted that all it does is remove the package from the system. So any configuration or package files would be left behind.
- The command `sudo apt-get purge package` is the correct way since it also deletes the other small-minor files.
- The command `sudo apt-get autoremove package` is used to remove a package as well as its corresponding dependencies.
- The command `sudo apt-get clean` removes all the installed packages from the system.
- The command `sudo apt-get autoclean`is used when only the packages that have become stale are to be removed.