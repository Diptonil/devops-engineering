# Handling Collections

Collections of data are handlied using native data structures that vary with every language. However, some constructs are always common: arrays, lists, hashtables, etc. Go has support for arrays, slices and lists, which we would see in the preceeding discussion.


## Arrays

- Arrays in Go are similar to its original definition (how it used to work in C or Java).
- To declare (this sets the default values in array to the zero values of the corresponding data type):
    ```go
    var variable [5]int
    ```
- To assign values and declare:
    ```go
    variable := [5]int{1, 2, 3, 4, 5}
    ```
- To assign values and instead of doing the count manually, letting Go figure it out on your own:
    ```go
    variable := [...]int{1, 2, 3, 4, 5}
    ```
- To declare and array and assign specific values and letting the rest be their defaults (only index value of 1 and 3 is filled up here):
    ```go
    variable := [5]int{1: 10, 3: 30}
    ```
- Accessing values is similar to other languages.
- We can copy arrays around. Ensure that capacity and types are similar. This is done like:
    ```go
    variable := [5]int{1, 2, 3, 4, 5}
    var variableCopy [5]int
    variableCopy = variable
    ```
- Two dimensional arrays can be made as:
    ```go
    var array [4][2]int
    array := [4][2]int{{10, 11}, {20, 21}, {30, 31}, {40, 41}}
    array[2][0] = 69
    ```
- We can pass around arrays using 2 methods: *pass by reference* (using pointers) or *pass by value* (using the entire array). This is how we do *pass by value*:
    ```go
    array := [4][2]int{{10, 11}, {20, 21}, {30, 31}, {40, 41}}
    Func(array)

    func Func(array [4][4]int) {
        ...
    }
    ``` 
<br />The use of pass by value might be undesirable since the whole data gets copied first for being passed to the function. This doesn't happen in pass by reference. A one million sized integer array, for transaction between functions would only take 8 bytes rather than 8 million bytes. Pass by reference:
    ```go
    array := [4][2]int{{10, 11}, {20, 21}, {30, 31}, {40, 41}}
    Func(&array)

    func Func(array *[4][4]int) {
        ...
    }
<br />What we need to keep in mind here is that altering the value of the array, even within the function would disrupt the actual data structure since reference is being shared (the actual thing itself).