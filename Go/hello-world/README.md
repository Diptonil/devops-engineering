# Basic Hello World

The following considerations are made to create this project:
- In this directory, run `go mod init github.com/Diptonil/devops-engineering/tree/main/Go/hello-world`.
- The `go.mod` is a file that tracks dependencies, versions and other metadata.
- In the root, we are to create a file. We cannot name it anything we want. Since we would only have 1 file, that has to be `main.go` containing the `main()`. We would type out the code in here.
- This is how we use `go mod init` for more complex projects. We can run commands like:
    - `go run .`
    - `go build .`
    - `go vet .`
    - et cetera.
  The commands that we actually run are (here we aren't concerned with building the files as much as just running it):
    - `go fmt .`
    - `go run .`
- The reason to have such a huge name was to follow the convention of dependency tracking. The module should have a name that pointed to the location where its code was kept online.


## Adding Something More

- We add an external dependency: `rsc.io/quote`. This module has a function called `Go()` in its package `quote`.
- This function just returns a simple string, nothing more. 