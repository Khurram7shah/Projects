#Mad libs Python Project 
 
print("Welcome to the Mad Libs game!")

name = input("Enter your name: ")  # Get input name from user
print("Welcome", name)
Age = input("Enter your age: ") #get input age from user
print("Oh, you're so young", name)
place = input("City: ") # Get input "age" from user 
adjective = input("Enter your Favrait Celebrity: ") # Get input from user
noun = input("Enter your favorite food: ")   # Get input from user

madlib = (f"Hello, my name is {name}! My age is {Age}. I live in {place}. My Favroit Person is {adjective}. I love {noun}.") # Use f-string for embedding expressions inside strings.
print(madlib)   