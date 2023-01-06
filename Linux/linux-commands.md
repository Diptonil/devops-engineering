# Linux Commands

Here we list out some famous Linux commands that quite hndy in day-to-day operations. However, the detailed description can be obtained easily using the `man` command (the Linux Manual).


## Commands

- `man`: To operate on the Linux Manual.
- `echo` Display to console.
- `sort`: Sort file contents.
- `ls`: List out directories.
- `rm`: Deletion of files or directories.
- `mv`: Moving files and directories to a certain destination.
- `less`: Lets us view files in a more sophesticated manner.
- `head`: Shows us first few lines of an output stream result.
- `tail`: Shows us last few lines of an output stream result.
- `wc`: Used to obtain word counts.
- `cat`: For reading, writing & concatenations.
- `tac`: To reverse whatever file is read.
- `rev`: Can reverse contents in each line.
- `tee`: For piping as well as processing.
- `xargs`: Converts bare piped data into command line arguments.
- `cut`: Columnize and segregate data so as to retrieve parts of it with ease.
- `cd`: Change working directory of terminal.
- `cal`: Calendar.
- `clear`: Clears screen.
- `date`: Displays time and date.
- `history`: Shows the executed command history.
- `exit`: Exits terminal.
- `which`: Searches and shows the path to a particular command.
- `pwd`: Used to print working directory.
- `chmod`: To alter changes of permissions of a certain file/ directory.
- `type`: Informs about the file type.
- `mkdir`: Creates a directory.
- `touch`: Creates a file.
- `vi`: Opens up the Vim editor.
- `nano`: Opens up the Nano editor.
- `locate`: Used to find files in the system.
- `find`: Perform search tasks in the file system.
- `updatedb`: Used to update the search database that `locate` accesses.
- `sudo`: Used in conjunction to other commands to allow elevated system privileges.
- `tar`: Used to archive files.
- `vmstat`: Used to monitor performance as it gives information about processes, memory, paging, etc.
- `free`: Shows memory details.
- `dmesg`: Shows kernel log messages.


## General Guideines

- If some commands don't work with the given options, try to switch the options before further troubleshooting.
- Concepts of wildcards, redirections, piping, brace expansions, etc. are applicable not just to specific commands but all possible scenarios that seem logical in Linux.


## Command Aliases

- Command aliases allow us to run extremely tedious and long commands as customised, small commands that we choose (like alisaing in C language).
- In Home, the `.bash_aliases` file needs to be created.
- In the file, we write an alias like:
```
alias smallName='extremely large command'
alias getdate='date | tee home/userName/file.txt | cut --delimiter="  " --fields 1 > weekday.txt'
```
- We need to reload our command for the alias to get loaded.
- Aliased commands can also be pipelined.