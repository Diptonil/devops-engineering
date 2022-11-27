# Special Files in Linux

Most of the important special files in Linux let us leverage certain functionalities that may make lives easier for us if handled well. Those files are mostly hidden. One such file that has been explored in the section of Linux Terminal is the `.bash_aliases` file.


## The `.profile` File

- These files are primarily used to set environment items for every user.
- Like `autoexec.bat` file of DOS, it is a start-up file for an UNIX user. It is located in the `~` directory.
- `.profile` is executed by bash when you get a normal shell process like opening a terminal tool.
- When we export an environment variable, it gets stored here.


## The `.bashrc` File

- This gets executed everytime a system boot happens.
- We can add custom environment variables here.