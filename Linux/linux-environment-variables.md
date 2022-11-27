# Linux Environment Variables

Some environment variables are used frequently to derive details about the state of the system or other relevant information. They can be Commonly used variables are listed here. We can declare our own variables just like how we would do in a Bash script: `variable=value`. However, this would only create a temporary regular variable that cannot be used by child processes (like other Bash scripts, SSH sessions, for example). Their values would also be lost when system boots. To make it available to all child processes, we use `export variable=value`. However, the variable will still go away if we logout. To make it a permanent environment variable that sticks around, we edit the `.bashrc` file and append `export variable` to the end of the script. So, when we login from the next time, the variable would stick around.


## SHELL

This shows the selected Shell that we have been using. Defaults to Bash.


## USER

This shows the current user.


## PSD

This is similar to just entering the command `pwd`.


## HOSTNAME

This is the name of the machine that you are on. The `user@machine` text that precedes every command uses the hostname for the `machine`.


## PATH

Every command in Linux is actually a program that is stored at a particular laocation. That program is written as a shell script and may accept arguments as well (options or file names or locations, etc.). So Linux needs a way to recognize if a certain command is indeed a program. If the path of the shell script of that command is registered (appended to the list) to the PATH variable, the command shall get recognised. <br />
For example, when we install Python, we cannot really work with it unless we add the location of its binary to the path. This also follows in Windows.


## RANDOM

Pseudo-randomly generates a number between 0 and 32767.