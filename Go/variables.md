# Variables & Types

There are many ways to declare Go variables. We can adopt to any standard. It is, however, recommended to stick to one standard unless we need to gain certain advantages over our default.

- If we are declaring a variable, we must use it. If not, we get a Compile Error. Go does this to ensure code quality.
- **Declaring & Assigning Variables**:
    ```go
    // Best used in cases where we just declare and assign simultaneously. The other form isn't used in that case.
    variable := 420
    var variable2 = 69
    var variable3 int = 9
    ```
- **Declaring**:
    ```go
    // Best used in cases when we first declare and then assign somewhere else.
    var variable string
    variable = "initial"
    ```
- Whenever we use `:=`, we must assign. We cannot declare any values without the `var` keyword.
- Go is type inferred but we also have the added flexibility of choosing and setting types. This is to ensure that we have the best of both worlds and errors can be minimized, giving us full control.
- Sometimes we do want to be specific with the data type we are defining, rather than letting Go infer it. We may choose to assign a trivially simple value initially, only to let it transform into something more complex. In these cases, it is best to define and assign (the latter approach from above).


## Identifier Conventions

- If we follow `camelCase` for naming, it is private identifier that doesn't get exported. If we follow `ALLCAPS` or `PascalCase`, that identifier would get exposed to the people importing the package.
- `ALLCAPS` in official Go docs are used only in cases when we need to import a POSIX or OS-supported constant. In all other general cases, `PascalCase` is followed, even for constants.
- Go indentifiers generally stick to shorter names (in no way does it mean that they shouldn't be descriptive).
- For useless identifiers that don't get referenced (like iterators, etc.), we use `_` like we do in Python.
- Whenever, in the beginning of a program or wherever, we have a lot of declarations of variables, we use a `var` block. It is like this:
    ```go
    var (
        // all declarations and assignments (if any)
    )
    ```


## Constants

Everywhere a variable is declared, we can use `const` in place of `var`.


## Data Types

We have the standard types as:
- `bool`
- `string`
- `int`: This stores a 32-bit value in 32-bit systems and a 64-bit value in 64-bit systems. For every use-case, unless we have a very specific reason, we should stick to `int`s rather than using `int16`, `int8`, etc.
- `uint`: Unsigned integers are the ones that have double the limit of a regular integer, with the cost of not having the ability to store negative integers.
- `int64`
- `int32`
- `int16`
- `int8`: Aliased as a byte.
- `float32`
- `float64`
- `complex64`
- `complex128`


## Printing Out Types

- We know the basic functionality of `Println()` in `fmt` package. It also serves a purpose of showing what type of data is stored in a variable. This can be helpful to:
    - Learn more about the types of data supported by Go.
    - Know the type of data stored by a type inferred variable.
- We do that by using the `%T` placeholder. This is shown in:
    ```go
    var n2 int32 = 9
    var n3 int64 = 9
    n4 := 9

    fmt.Printf("%T %T %T", n2, n3, n4)
    ```
- The output shall be: `int32 in64 int`.


## Type Casting

For explicit type conversions (wherever possible) between floats and ints, et cetera, we use the data type as function names:
- int(): For converting into ints.
- float32(): For converting into float32.
- float64(): For converting into float64.