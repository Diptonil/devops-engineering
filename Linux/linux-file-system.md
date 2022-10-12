# Linux File System

Files are, in some way or the other, something that we would be dealing a lot in Linux for DevOps purposes. Certain nuances of the whole architecture, if understood, can simplify DevOps tasks as well as enable engineers to understand the work of others as to the handling of files and various other features and functionality of Linux.


## General Observations

- All hidden files start with a dot ('.'). They can be accessed in the terminal using the -a or -A option of the `ls` command.
- The green-coloured text at the left that appears at the execution of every command is called the *Shell Prompt*. It can tell us where we currently are. The left-most text tells the name of the looged-in user and the name of the computer (separated by an '@' symbol). After the colon, we have the path where we are at. The tilde ('~') suugests that we are in the home directory of the current user. It is short for `/home/user`. In fact, the `~` and `/home/user` can be interchangibly used.
- Every time we first log in, we start from the home directory of the user.
- The base directory is where everything starts from. In that we have the home directory, within which we have the user directory.
- Everything in blue is folders while files are shown in white. Programs are coloured as green. Archives are shown in red.


## File Extensions

- In Linux, files are not judged by their extensions at the first glance, even if it might appear to be so (in the GUI).
- A file has a certain header for Linux to tell if if it a PNG or a PDF or whatever else. Just by changing the extension, we are merely changing the way we want the file to be executed. That does not guarantee a change that the file becomes a PDF from a TXT even if we succeed in renaming. The header is the de facto in deciding the type of file it is.
- The `file` command can analyse a file given as the input argument and give a report accordingly.
- Changing extentions to change file types for whatever purposes never really work. So doing that will only cause troubles. Converters are more beneficial in this context.
- If any software (not tied to the OS directly) cannot recognise the file extension, it falls back to the default extention and tries to execute it according to the way it is meant to be executed. Such executions may or may not work.
- We can leverage the previous point to actually create files with human-readable extentions that cause no error or conflict upon executions. Examples: `log.debug`, `log.success`, etc.


## Wildcards

- Used in conjunction with search or list commands, they can be a powerful tool to narrow down results and show us a subset corresponding to what we want to see using Regex.
- The asterik/ star ('*') wildcard matches anything that we want to see. For example, if we want to see files or folders beginning with a 'D':
```sh
ls D*
```
We can, of course, use it to catch hold of things with definite ends as well (like `ls *.txt`).
- The question mark ('?') is used as a placeholder for any character for a file/ folder being searched. Example:
```sh
ls He?.txt
```
This returns us all files named as Hex.txt, Her.txt, Hem.txt, etc. We can add more than one '?' as well.
- The square brackets ('[]') is used to match all the occuring characters given inside the brackets.
```sh
ls file[123456789].txt
# We can also write `ls file[1-9].txt`
```
This would return file1.txt, file2.txt, and so on. Combinations like [a-z], [A-Z], [0-100], etc. are all possible.


## Creating Files & Folders

- We can use the `touch` and `mkdir` commands for the same. However, we can alternatively use `echo` or `cat` commands with redirections to create non-empty files.
- We cannot create files/ folders with spaces. If we do so, we would end up creating two/ more different entities. The correct way to deal with spaces is:
```sh
mkdir "folder one"
#... and not `mkdir folder one`
```
- It is possible to do bulk creation of objects using *Brace Expansion*. It works on the principle of algebraic bracket expansions. For example, if we write something like:
```sh
mkdir {bat,spider,ant}_{1,2,3}
```
This would give us folders with names `bat_1`, `bat_2`, `bat_3`, `spider_1`, and so on. Care is taken not to apply whitespaces in between anything. We can also change the underscore to something else if we wish to in the command. The folders would be names accordingly.
- If we are to make files within all these folders in bulk, we would execute something like:
```sh
touch {bat,spider,ant}_{1,2,3}/file{1...10}.txt
```
This gives us 10 files (`file1.txt`, `file2.txt`, etc.) inside all the folders.
- The concept of *Brace Expansions* are not restricted just to creation of files and folders. It also extends to other parts of Linux.


## Locating Files

- The `locate` command in Linux works by scanning the database file in the system that holds all information about the files and directories on the system.
- This uses Regex to search up the files and outputs the path where it can be found. One can use options to minit the search results and also to toggle case sensitivity, etc.
- The database queried doesn't get updated often in a day. So all changes happening don't get reported to it at all times. So locate command may be ineffective in some cases. We may use certain options that allow us to check if the query results actually exist before showing them to the output stream, and more options. It is generally recommended to use the `--follow` and `--existing` options.
- We can update the database using the `updatedb` command. It is daily run by a cron job to ensure that all the entries are refreshed but we can coerce a run as well. It does require administrative privileges. So we generally use `sudo updatedb`.


## Finding Files

- It does not need a database to work. It can just work then and there for any types of searches.
- It can perform more sophesticated queries, albeit slower.
- It lists out all the files and folders, given a search path (a directory to start from). It shows the information to the maximum possible depth. All subfolders are explored.
- We can also control the maximum search-depth using options as well as choose the type of objects (files/ folders) to find.


## File and Folder Permissions

- We can know about the permissions of the contents in a directory by the `ls -l` command.
- The permissions are displayed in the manner of: `drwxr-xr-x`.
- If the first flag is set to 'd', the object is a directory. If it is a '-', it is not one.
- If the second flag is set to 'r', the object can be read by the current user. If it is a '-', no read access is given.
- If the third flag is set to 'w', the object can be written to by the current user. If it is a '-', no write access is given.
- If the fourth flag is set to 'x', the object can be executed by the current user. If it is a '-', no execute access is given.
- The above sequence of three entries repeat themselves thrice (there exist nine 'rwx'). So apart from 'd', there exist nine flags in total. From left to right each set designate the permissions for owner, group and other users. The permissions can be changed using the `chmod` command, given we have access to the file or directories.
- After that comes the name of the owner of the object.
Right after that we have the file size.
- After that we have the date and time for last alteration.


## Tab Completions

- Typing out relative paths with the `cd` command may at times be tedious when the destination is somewhat far.
- To save us time, we can use the Linux autocomplete feature of tab completions.
- After slash, we write out the first character of the folder in which we want to go and hit tab. If no conflicts are found, Linux autocompletes the folder name with the one that begins with that character. If there exist multiple folders starting with that character, try hitting tab after typing out some more characters until there are no more conflicts.
- This speeds up traversing directories.
- Tab completions can be used in conjunction with other commands as well for file-name completions.


## Root Permissions

- At the base level, if we try to enter the root folder using the simple `cd` command, we may be denied permission.
- This means we can access only parts of the Linux file-system that we have access to.


## Archiving into Tarballs

- A tarball is a certain space where data is collected so that it may be, in further processes, compressed using various compression algorithms.
- So, the whole process involves making up a tarball for compression, firstly. Secondly, using an algorithm to compress down the files.
- Syntax to make a tarball out of three files:
```sh
tar -cvf archive.tar file[1-10].txt
```
This asks the command to operate with verbosity (not just finish the operation without any message logs) given by the '-v' option. The '-f' option tells that files are to be collected. The '-c' option tells the system that we need to create a new archive. The created tar is named as `archive.tar` and the files mentioned alongside can be considered as the ones that get archived.
- Archives cost more memory than the sum of its components. This is because some data is additionally added to mention that the object is a tar archive. Upon compression, it shrinks.
- To check the files that are available in a tarball:
```sh
tar -tf archive.tar
```
- Syntax to extract a tarball:
```sh
tar -xvf archive.tar
```
The '-x' option is for extraction.


## Compression

- There are many compression algorithms that can reduce the size of tarballs. The ones explored here are: GZIP and BZIP2.
- GZIP is faster but has less compression power while BZIP2 has higher compression power but takes more time.
- To use GZIP:
```sh
gzip archive.tar
```
A file called `archive.tar.gz` is given out.
- To extract the GZIP compression into a tarball:
```sh
gunzip archive.tar.gz
```
- To use BZIP2:
```sh
bzip2 archive.tar
```
A file called `archive.tar.bz2` is given out.
- To extract the BZIP2 compression into a tarball:
```sh
bunzip2 archive.tar.bz2
```
- There exist Zip files on other OSs commonly where the Linux archives do not tend to work well. It is a one step process where we directly zip a set of files and is similar to the `tar` command.