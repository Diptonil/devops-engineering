# Golang

In this section, a basic introductory discussion to Go would be explored. The discussion, however, would not be restricted to as much knowledge as would be necessary for working in the field of DevOps. Developmental concepts are explored as well so as to gain insight on how complex applications like k8s are actually built.


## Why Go?

- Every language used within the codebase of most Google applications (Java, Python, C/C++) had some limitations. Python was slow. Java had too much boilerplate and the environment had increasingly become complex as the newer versions had come out. C and C++ had compile-time issues.
- Go was designed to provide a solution to it. It takes all their strengths and combines them together, keeping the weaknesses away. It is quite high-performance.
- The best things about Go would be its speed, type-systems as well as (most importantly) support for concurrency. This is done using goroutines, which run within threads (it eliminates the need to multithread the application). Communication is also possible between the goroutines. That is done using channels.
- There are many things that Go has that might not make sense if the teachings of some prior language is held on to. The best way to learn it would be to start with a blank slate.


## Cons

- Has a steeper learning curve as compared to languages like Python.
- Not suited for beginners.
- Using Go can be time-consuming and frustrating. In some cases, programmers will need to use more lines of code than in a normal situation.
- Things that can be easily done with languages like JavaScript or Python with such a huge ecosystem require too much of work here.
- It’s got defective dependency management.


## Contents

1. **The Go Command**: Exploring the `go` command.
1. **Hello World Project**: A Go project to print Hello World.
1. **Variables**: Seeing how variables, data types & constants are defined in Go.
1. **The Math Library**: A basic understanding of the semantics and the types of operations that can be supported.
1. **Strings**: A basic understanding of how to operate on strings in Go.
1. **Pointers**: 
1. **Collections of Data**: Seeing how arrays, slices and lists work in Go.
1. **Errors**: Exploring more about errors.


## Accepting Console Input

- The `fmt` package has the `Scan()` function. It works similar to C-language's `scanf()`. Example: `fmt.Scan(&variable)`.
- We see that we are using pointers here, like C. The reason for use of a pointer here and not during printing is that the value is being dealt with in printing. Here, we are actually taking a variable and storing a value inside it at its memory location.
