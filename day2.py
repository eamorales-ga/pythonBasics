# Description: This file is for the second day of the python workshop


# create variables for the following :
# 1. age
age = 16 #integer variable
# 2. name
name = "John" #string variable
# 3. song
song = "Happy Birthday" #string variable
# 4. food
food = "apples" #string variable
# 5. number
number = 100 #integer variable
print("Once upon a time, there was a " + str(age)+ " old coder named " + name + ".")
# #now include the variables you just made print in the following...
print(f'''Once upon a time, there was a {age} old coder named {name}.
{name} liked to hum the song {song} while coding. It was so annoying that their teammates would
throw {food} until {name} would stop singing.
Still, {name} was the best coder on the team and could write {number} lines of code every day.
Maybe {song} was {name}’s secret power?''')
#f strings are a way to format strings in python
# No one will ever know.


# What is syntax ? What is an algorithm?
#syntax is the way we write code 
#in javascript we would write a variable like this
#var name = "john"
#in python, we would write it like this
#name = John
# what is a variable? What is a string?

# strings are nothing but plain text
# what does this do?

print("Giraffe \n academy")
#/n is a newline character

# or this
phrase = "python learning"
print(phrase + " is cool")
#what does the + sign do? What is it called?
#it concatenates strings

#what if I wanted to get the length of a phrase?
print("the length of the string is " + str(len(phrase)))
declaration = '''Once upon a time, there was a {age} old coder named {name}.
{name} liked to hum the song {song} while coding. It was so annoying that their teammates would
throw {food} until {name} would stop singing.
Still, {name} was the best coder on the team and could write {number} lines of code every day.
Maybe {song} was {name}’s secret power?'''
print("the length of the string is " + str(len(declaration)))


#what if I wanted to make the letters in the variable upper case or lower?




#what if I wanted to check and see if the phrase was all lower or upper?


#What if I wanted to get one letter of the phrase


# The names you use when creating these labels need to follow a few rules:
# 1. Names can not start with a number.
# 2. There can be no spaces in the name, use _ instead.
# 3. Can't use any of these symbols :'",<>/?|()!@#$%^&*~-+
# 4. It's considered best practice (PEP8) that names are lowercase.
# 5. Avoid using the characters 'l' (lowercase letter el), 'O' (uppercase letter oh), or 'I' (uppercase
# letter eye) as single character variable names.



# Working with numbers bold text
# We'll learn about the following topics:
# 1. Types of Numbers in Python
# 2. Basic Arithmetic
# 3. Differences between classic division and floor division


# Addition

# Subtraction

# Multiplication

# Division

# Modulus

# Exponentiation

# Floor Division

# Order of Operations followed in Python

# You can use parentheses to specify the order in which you want operations to be performed.

#to do more you need to import special math libraries from python
#from math import *
#this goes out and grabs some different math functions we can use
#floor method
#ceil method
#sqrt method
from math import * #import everything
print(floor(95.76666))
print(ceil(98.3333))
print(sqrt(54))


# Python has various "types" of numbers (numeric literals).
# 1. We'll mainly focus on integers and floating point numbers. Integers are just whole numbers,
# positive or negative. For example: 2 and -2 are examples of integers.
# 2. Floating point numbers in Python are notable because they have a decimal point in them, or
# use an exponential (e) to define the number. For example 2.0 and -2.1 are examples of
# floating point numbers. 4E2 (4 times 10 to the power of 2) is also an example of a floating
# point number in Python.



# challenge exerces... 
#create a program that asks for the user's name and age and then prints out the user's name and age

# create a program that asks for the user's name and then prints out the user's name in all caps

# create a program that asks for the user's name and then prints out the user's name in all lower case

# create a program that asks for price and then prints out the price with a 10% discount

# Given the phrase "Hancock High School", perform the following operations:
# Print the phrase with a newline character to separate "Hancock" and "High" and "School".
# Concatenate the phrase with " is cool", and print the result.
# Print the length of the phrase.
# Convert and print the phrase in uppercase and lowercase.
# Check if the phrase is all lower or all upper and print the result.
# Print the first and the last letter of the phrase.