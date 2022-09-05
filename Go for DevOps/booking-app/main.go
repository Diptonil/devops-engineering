package main

import "fmt"

func main() {
	const programmeName = "DevOps Campaign"
	var learnerName string

	fmt.Printf("Hello! Welcome to the %v! This section is particularly aimed at learning Go from a DevOps perspective.\n", programmeName)
	fmt.Println("Please check out the README.md of this directory to go through the technicalities of Go within two minutes. Prior programming experience in C or Java would certainly help.")
	fmt.Println()

	fmt.Print("Please enter your name: ")
	fmt.Scan(&learnerName)

	fmt.Println("Your name is", learnerName, "and is stored in the memory location:", &learnerName)
}