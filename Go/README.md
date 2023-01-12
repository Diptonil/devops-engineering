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
1. **Pointers**: 
1. **Collections of Data**: Seeing how arrays, slices and lists work in Go.


## Initializing a Project

- The primary file that gets run in a Go project is the `main.go` file. Every project has one.
- A Go file cannot work without being a part of a project. We need a *module* for a Go file to run. To create a module, from within the root of the project directory: `go mod init project-name`.
- A `go.mod` file is created. It would have the Go version and the module name describing the project.


## Packages

- All Go code must reside within packages. The package to which the `main.go` file belongs is the `main` package. This is why the first statement of every Go file is a package declaration.
- Everything in Go is segregated into packages. Unlike Java's `java.lang`, nothing is pre-imported. We have to explicitly mention every imports. Import statements come after the package declaration.
- For example, consoling in Go involves importing the `fmt` package and using the `Println()` or `Print()` within it. If variables are being used, it may be written as: `fmt.Print("Hello, there. How are you,", studentName)`. Note that spaces are automatically appended after a quote-end. This might be undesirable as well in some cases.


## Printing to Console

- The `fmt` package provides `Print()`, `Printf()` and `Println()` functions.
- They work the same way they work in Java.
- `Printf()` is the print formatting function that works exactly similar to the C-language `printf()`.
- To use `Printf()` in conjunction with newlines, escape sequences (\n) may be used.
- Here the placeholder value is always considered as `%v` (this means the value) instead of `%s` for strings, `%d` for integers, etc. as was the case in C.
- We also have another placeholder - `%T`. This is for types and not values (`int`, `string`, etc.).


## Accepting Console Input

- The `fmt` package has the `Scan()` function. It works similar to C-language's `scanf()`. Example: `fmt.Scan(&variable)`.
- We see that we are using pointers here, like C. The reason for use of a pointer here and not during printing is that the value is being dealt with in printing. Here, we are actually taking a variable and storing a value inside it at its memory location.


## Calculations

Compilation errors may happen in case of type mismatch. For example, `uint` and `int` are different and they would give compiler errors if not handled well.
