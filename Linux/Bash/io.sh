#!/bin/bash

echo "What is your name?"
read name
date=$(date)
echo "Hello, $name!"
sleep 2
echo "Current date and time is: $date."
sleep 2
echo "Bye, $name."