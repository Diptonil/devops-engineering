# The Go Command

The `go` command serves a lot of purposes, besides doing code buidling, compilation, etc. It is a tool that offers a suite of functionality that we can use. Here, we enlist them.


## `go build`

- If we have a simple program, we can just run `go build file.go`. That builds the file and produces an executable.
- What exactly gets built? A package. So, any normal standalone file that is being built must belong to the main package, having a `main()`.
- The executable can be executed accordingly with respect to the OS they work on.


## `go clean`

- When we have an executable of a Go file and we would like to clear it out for version control or anything else, we can run `go clean file.go`. The executable gets destroyed.


## `go run`

- This is the command that combines building and executing a file together, upon executing `go run file.go`.
- This doesn't keep any executables lying around. Exceutables are mostly used in cases when the final build is to be released.


## `go vet`

- This command is used to check code for common errors. The types of errors `go vet file.go` can catch:
    - Bad parameters in Printf style function call.s
    - Bad struct tags.
    - Unkeyed composite literals.
    - Method sinature errors for common method definitions.
- It is not a failsafe from creating buggy and erraneous code (huge logical flaws).
- It saves the wait time to build files. Less overhead is associated since an executable is not actually being produced.
- It is a good idea to vet files before making commits.


## `go fmt`

This command simply formats the existing code to follow a specific guide of format. This eliminates any heated discussion on style and conventions when `go fmt file.go` is executed. This is another command that goes well before version control commits.


## `go doc`

- This is used to open up the official docs with respect to any package or anything as such.
- Use `go doc <package-name>` or any other resource that needs to be accessed and read about.
- This eliminates the need to browse the construct that one would feel doubtful in.


## `go help`

- This command is used to list out additional help topics and commands that we can look at for more info.
- We can see the utilities offered by `go vet` by running `go help vet`.


## `go mod init`

- The practical example of `hello-world` would introduce one to how exactly this command works and with what.
- The command for something like that should be `go mod init github.com/Diptonil/repo-name`.
- This produces a `go.mod` file that keeps track of all the dependencies and imports.
- The custom is that we only name our package something that:
    - Some unique name across all of Go so that name found is really unique.
    - The absolute path to the place from which he can actually be downloaded. A GitHub repo can also be an example here.
- We can take any regular name for packages as such. But it is generally recommended that we have some customs in place whevever some are meaningless.
- We need to have a `main.go` to build it.


## `go mod tidy`

This command scans through all the sources and then updates the `go.mod` file with all the required dependencies.


## `go get`

- This is similar to the `pip` command in Python. Used to download external dependencies.
- This command, when run for the first time, would generate a `go.sum` file. This file is a lot like `requirements.txt`, but not exactly.


## The Godoc

Sometimes, having a custom self-browsable documentation may help. We may start up a `godoc` server to host Go docs.
- Use `godoc -http=:6060` to start it up at 6060 port.
- This tool is responsible for all sorts of documentation, which means the docs of the currently created programs as well.
- If proper conventions in code are followed, `godoc` translates the appropriate comments, etc. into docs.
- Rules to document project:
    - Immediately above every identifier, start putting comments (single-line, multi-line, whatever).
    - It is important to realize that the comment should be located right above/ before the identifier.


## The `go.mod` File

This file is for dependency management. A module by definition is a collection of related packages with go.mod at its root. Both thi sand `go.sum` files should be checked into version control. The `go.mod` file defines the:
- Version of Go with which module is created.
- Module import path
- Requirements from external modules and their corresponding versions, which gets locked so that no errors due to dependency doesn't occur. Only direct dependencies are recorded.

There can exist cases when an indirect dependency is also included in `go.mod`. Any indirect dependency which is not listed in the go.mod file of your direct dependency or if direct dependency doesn’t have a go.mod file, then that dependency will be added to the go.mod file with `//indirect` as the suffix. We will see an example of this later in the article to know this better.


## The `go.sum` File

This file lists the checksums for all the dependencies (direct and indirect). The checksum present in go.sum file is used to validate the checksum of each of direct and indirect dependency to confirm that none of them has been modified. Dependencies ar of types:
- **Direct**: Dependencies defined by direct imports.
- **Indirect**: Dependencies of the direct dependencies.
