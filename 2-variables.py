
import string
from tokenize import String

'''
A variable (shown below) is something that stores data. Think of it like a basket that can hold fruit.

The basic syntax to declare a variable is this:

<variablename> = <variablevalue>

In other languages you may need to specify the type:

<variabletype> <variablename> = <variablevalue>;

Notice the semicolon. Most languages require you to put a semicolon to specify the end of a line of code.
In Python, we use newlines and indentation instead of semicolons and curly braces ({})

There are two types of data types: primitive and non-primitive. Primitive data types
are only made up of one value, like only a whole number, a decimal, or a character. Non-primitive
(or civilized, I like to call it) stores multiple values, like several characters or an array of variables.

For example, an integer (int) is a primitive data type as it only stores a whole number. A character (char)
is also a primitive data type because it only stores one character. A boolean (bool) is a primitive data type as
it only stores a true/false value.

A string is the most common non-primitive data type. It is non-primitive (civilized), as it stores multiple characters 
(chars). An array is also non-primitive, as it stores multiple variables. An object is also non-primitive, as
it is used to access a class with static variables/methods. We will learn about objects later on.
'''

a = 9 
txt: String = "hahahahahahahahahahaha" # this is a group of characters, called a string. 
myChar = 'e' # this is a character
isCodingGood = True # this is a boolean, it stores true/false values.
myFloat: float = 4.555555555555555 
myDouble = 5.66666666666666666666

'''
In python you don't need to specify the data type of a variable; you just need <variablename> = <variablevalue>
This is great for beginners but not ideal for those who are more advanced. You can specify the type like this:

<variablename>: <variabletype> = <variablevalue>

You may need to import stuffs like string. Just add this to the top of your file:

import string

If you want to learn more advanced syntax, try learning C#. C++ and C have advanced syntax, but C does not have classes,
only structs.

'''
print(txt + " thank you") #con cat e na tion , concatenation (mixing string together to form a string)

