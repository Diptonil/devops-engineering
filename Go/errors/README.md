# Errors

The `errors` package is used for handling errors. Error handling in Go is quite different from other languages with respect to the fact that it doesn't seem too mature. It is also one of the most controversial things in Go that cause developers pain. Error handling is quite important to safeguard code from breaking at critical instances like:
- File reading
- Managing database connections
- Servers, etc. <br />
The `main.go` file provides a glimpse on how to create a custom error for use.


## Some Tips

- Handle errors in code as early as possible. Nesting logic within and going on about it, without doing error checks is not recommended. The rule of thumb is to do it immediately.
- If we have a same custom error being used multiple number of times in a lot of different places, it is worth creating a package level variable that stores the newly created error.
