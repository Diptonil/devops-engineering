# The Linux Terminal

Pop open the terminal by pressing `Ctrl` + `Alt` + `T` in a Linux machine. Before that, we look at some very basic rules that applies to the whole setup of a terminal as well as what exactly commands are. Only a few commands with added nuance are explored. The rest should be studied and experimented using the manual.


## Basic Rules

- If `command not found` is displayed, either there is a typo in the command or the command does not exist in reality or the command in question is a third-party tool that has not yet been installed in the system, due to which the terminal cannot recognise it. The solution to that would be to install it using certain commands that would be discussed later.
- Commands are case sensitive.
- We can cycle up to the past commands using the arrow up key. This depends upon the `history` command.
- Use the `&&` operator to chain commands. Example:
```sh
git add . && git commit -m "Example to illustrate command chaining"
```
- In Linux, we can customise the commands using **options**. They are flags that can be applied after using a `-` operator.
- Certain commands may accept more than one options at a given time. We may specify it like this (assuming that the options for the example command is valid):
```sh
command -a -b -c
```
We may also chain the options as:
```sh
command -abc
```
- Some options may also accept inputs with the equal operator. This example shows the same by getting a month before and after (using A and B options) December, 2000.
```sh
cal -A=1 -B=1 12 2000
```
- Options exist as two types: longforms and shortforms. Shortforms are common and available for all the commands no matter what. They can be chained. The examples shown above are all shortforms. <br />
Longforms exist only for specific commands. They are used with two dashes (--). They cannot be chained. For example, to get universal time:
```sh
date --universal
```


## Commands

- Commands like `echo`, `ls`, etc. are all programs that are stored in the shell. When we install some new commands, they too are programs that get stored in our systems.
- They all reside within the `bin/` folder. This is
- The general format of commands are: commandName options inputs.
- For detailed info on the use of most commands, we are better off using the Man Pages.


## Terminal Shortcuts

- Open new terminal using `Ctrl` + `T`.
- Exit using `Ctrl` + `D`.
- Clear screen using `Ctrl` + `L`.


## Terminal Sessions

- We can spin up more than one terminal instances at any given time in case we have more work (one terminal to run a server, another to SSH into a system, another for general purposes, etc.).
- The `tty` command is used to find the root program that runs for a particular terminal and the associated path to it.


## The `history` Command

- This command shows the history of all the commands used in the current session (with no option by default).
- When we cycle through the commands, it is actually because the commands that we execute get stored in `~/.bash_history`. Which is a something that `history` is tied to.
- Instead of cycling all the way back up, when we know the list of commands we have used (this comes numbered), we can just reuse that command by referring to the history table. If we have the `git add .` command numbered as 9 in the history-table, we can reuse it by typing out `!9` and running it.
- To clear history, use the `-c` option. This is a temporary measure because when one logs out, the current shell's history is appended to `~/.bash_history`, which is a cache of previous shells' histories.
- To permanently delete history, use the command (we cannot cycle through the history anymore after this):
```sh
history -c && history -w
```


## I/O

- The *Standard Data Stream* is the channel that leads to the pipelining and interaction of the inputs and outputs. There are two types of outputs - the Standard Output Stream and the Standard Error. Standard Input is assigned 0, Standard Output 1 and Standard Error 2. The former is used when a command succeeds and a correct response is generated while the latter is used in case the inputs are wrong and erraneous.
- By default, the Standard Output, Standard Error and the Standard Input is connected to the terminal. The process to change where it connects to is called *Redirection*.
- The inputs to a command (or the options to a command) in the terminal are called *Command Line Arguments*.


## The `cat` Command & Output Redirection

- This command can be used to do a lot of things but is built on the principles of standard Linux I/O which actually lets it perform so many tasks by itself. It is a command that can accept input from Standard Input Stream and give output to Standard Output Stream. The reason why this command can take so many forms in its functionality is because of Redirection.
- The following example gives back the word 'meow' because the input as well as output both are connected to:
```sh
cat
meow
```
- To specify the destination to the Output Stream, we use the '>' operator. If file specified doesn't exist, it gets created and written to. If it does, it gets overwritten. We use the numbers (0, 1, 2) to signify the stream that we are working with (for the Output Stream, mentioning is optional). Here, 'Hello, world!' would get copied to file.txt:
```sh
cat > file.txt
#cat 1> file.txt
Hello, world!
```
- Redirection is not specific to the `cat` command. It is something that is done with any command imaginable using the two operators '>' and '<'.
- To tell the Redirection to not overwrite but to just concatenate, we would use '>>' operator. The file, if i previously existed, remains undeleted in terms of data:
```sh
cat >> file.txt
Bye, world...
```
- To Redirect a file as input to the default Output Stream (terminal):
```sh
cat fileName
```


## Error Stream Redirection

- Error redirection is mostly used in the process of logging error to a readable file during running of servers in the backend.
- Whatever error occurs in a command can be logged to a file using something like `2>> errors.txt`.
- To have the error message for the command below to be recorded:
```sh
ls --some-very-wrong-option WrongInput 2>> errors.txt
```
- We can do Redirection simultaneously in one line. Consider the use of the `history` command:
```sh
history 1> history.txt 2>> log.txt
```
This ensures that all the errors (if any) with the command get recorded in log.txt while the output gets stored in a simple file.


## Input Stream Redirection

- Input Stream Redirection proceeds with the use of the '<' operator instead of the '>' operator. To read from a file instead of the default input stream:
```sh
cat < file.txt
# cat 0< file.txt
```
- If we choose a different terminal to stream input to (using `tty`), we can do so using:
```sh
cat < file.txt > /dev/tty1
```
This would make the contents of file.txt to go over and get displayed to the terminal 'tty1'.


## Piping

- It is a process that makes it easier to pass a standard output of a command to another command's standard input.
- What we write as:
```sh
date > file.txt
cut < file.txt --delimeter "  " --fields 1 > file.txt
```
Can be written as:
```sh
date | cut --delimeter "  " --fields 1 > file.txt
```


## The `tee` Command

- This can be used to do both operations: execute a command as well as pipe the data that gets generated by the command to another input stream.
- For example, we have to save the date to a file as well as pipe it to the input stream of the `cut` command.
- The command is so names since its functionality resembles a T-pipe between two larger stream-pipes - two ends servicing different sections.
- To execute the example given above:
```sh
date | tee date.txt | cut --delimeter "  " --field 1
```
- If we wanted to continue the piping even further (resolve the data obtained after using `cut` into two other channels, presumably a file and another command), we can use `tee` again.
- We can extend this usability with different commands as well.
- The above operation can be done using the '&&' operators as well.


## The `xargs` Command

- Some commands do not really accept piped data. They strictly accept parameters (for example, the `echo` command). This command converts piped data into command line arguments.
- Example:
```sh
date | xargs echo hello
```
This outputs 'hello' first, followed by the piped-in date.
- One of the uses of this type of piping is to delete a bunch of files mentioned in a list using the `rm` command piped with `xargs`.
