package main

import (
	"errors"
	"fmt"
)

func main() {
	str := "This is a custom error that can live within an object. This is executed in the background by assigning this string as the error message of the error struct."
	errorObject1 := NewError(str)
	if errorObject1 != nil {
		fmt.Println("An error has occured:", errorObject1)
	}
}

func NewError(str string) error {
	return errors.New(str)
}
