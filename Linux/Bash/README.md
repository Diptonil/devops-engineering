# BASH

It was made in 1989 as an improvement over the already existing Linux Shell, and is aptly named as Bourne Again Shell. It wraps itself around the Linux kernel. More than its reputation of being a full-fledged programming language, it is referred to as a scripting language. It is extremely strong when it comes to leveraging the inner strengths of Linux and making work easier for everyone. It is a highly recommended skillset for Cloud or DevOps engineers and Network and Security Specialists for automating workloads or configuring networks, etc.


## Declaring a Bash Script

- The first line of a BASH script is always `#!/bin/bash`.
- `#!` is called a Shaban.
- This is the way we tell the interpreter which scripting language we wish to use to write our program. We may have a number of languages for our work. We may use Go, Python, etc. This line avoids all the confusion for the interpreter.


## Run a Script

There are two ways o do the same:
- Use `bash file.sh`.
- Use `./file.sh`. This is the way of telling the interpreter to "execute some file that is right here". However, initially, if we don't hvae execute permissions, we may have our access denied. We can simply use the `chmod` command as `chmod u+x file.sh`. It should work fine.


## Positional Parameters (Arguments)

Inputs that are passed along with the commands for execution as command line arguments are known as positional parameters. They can be accessed in the script as $1, $2, $3...


## Storing Command Output Within Variables

We just need to declare a variable and `variable=$(command)`. This would store in the variable the result of that command. The command could be anything that displays to the console: `whoami`, `date`, etc.


## Arithmetic

To do arithmetic in Bash, we use `$(( expression ))`. We can echo it out or store it in a variable. Refer to the 3rd script for better understanding.


## Example Scripts

1. `io.sh`: A sample script to display how I/O operations work.
1. `io-arguments.sh`: A sample script to display how arguments work.
1. `arithmetic.sh`: A sample script to display how 