# Golang for DevOps

In this section, a basic introductory discussion to Go would be explored. The discussion would be restricted to as much knowledge as would be necessary for working in the field of DevOps.


## Why Go?

- Every language used within the codebase of most Google applications (Java, Python, C/C++) had some limitations. Python was slow. Java had too much boilerplate and the environment had increasingly become complex as the newer versions had come out. C and C++ had compile-time issues.
- Go was designed to provide a solution to it. It takes all their strengths and combines them together, keeping the weaknesses away.


## Some Basic Norms

- Comments start with the usual double forward-slashes.
- Semicolons aren't needed. 


## Initializing a Project

- The primary file that gets run in a Go project is the `main.go` file. Every project has one.
- A Go file cannot work without being a part of a project. We need a *module* for a Go file to run. To create a module, from within the root of the project directory: `go mod init project-name`.
- A `go.mod` file is created. It would have the Go version and the module name describing the project.


## Packages

- All Go code must reside within packages. The package to which the `main.go` file belongs is the `main` package. This is why the first statement of every Go file is a package declaration.
- Everything in Go is segregated into packages. Unlike Java's `java.lang`, nothing is pre-imported. We have to explicitly mention every imports. Import statements come after the package declaration.
- For example, consoling in Go involves importing the `fmt` package and using the `Println()` or `Print()` within it. If variables are being used, it may be written as: `fmt.Print("Hello, there. How are you,", studentName)`. Note that spaces are automatically appended after a quote-end. This might be undesirable as well in some cases.


## Entrypoints in Go

Like Java's `main()`, Go also has its main method that serves as a single entrypoint to the execution of the project. There can only be one entrypoint to the application.


## Execution

Run `go run main.go`.


## Variables & Constants

- Go is statically typed. Use the `var` keyword to store values in variables. The convention is camelCase.
- If we are declaring a variable, we must use it. If not, we get a Compile Error. Go does this to ensure code quality.
- If we are immediately assigning a value to a variable right at the time of declaration, we do not need to specify the type. This makes it Type Inferred. Otherwise, we have to. We define type by specifying it after the declaration. Example: `var name string`.
- We have syntactic sugar to certain assignment cases for Go. Instead of writing `var name string = "Hola!"` we can write `name := "Hola!"`. This simplifies the use of the language and is more Go-like. Types cannot be explicitly defined in this case. Constants can't be defined like this.
- Using same conventions, if a value is to be used in an immutable fashion, we use constants. Use the `const` keyword instead of the `var`.


## Data Types

- Speaking about primitives, we have a whole range of types (like Java) from whose details we are abstracted away. These data types exist to ensure strict memory management. Good for programmers who like to be in charge. There are types like `uint8`, `uint16`, `int32`, etc. Such in-depth exploration may not be what we would need as DevOps engineers.
- We can also assign a value to a variable at the time of declaring it **with** a type: `var value uint16 = 100`.


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


## Pointers

Basically, pointers in Go are very similar to those in C/C++.


## Calculations

Compilation errors may happen in case of type mismatch. For example, `uint` and `int` are different and they would give compiler errors if not handled well.


## Arrays

We can create arrays here similar to C. We need to give the size as well, like: `var array = [10]` for a 10-element array.