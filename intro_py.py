#what is programming?
#programming is the process of creating a set 
# of instructions that tell a computer how to perform a task.
# These instructions can be written in a number of different "languages",
# or which are simply different ways of organizing the instructions and text.
# The set of instructions is often called a program or a script.
# The computer follows the instructions in the program one after the other, 
# until the end.
# The order of the instructions is crucial to the computer,
# and they are executed in a very literal manner.   
# Programming is a very creative and rewarding activity,
# but it can also be frustrating and time-consuming.
# If you have ever spent hours trying to find a missing semicolon,
# you will know what I mean.
# The computer will do exactly what you tell it to do.
print ("hello world")
########################
# Pyton Variable and Data Type ?
# Python has the following data types built-in by default, in these categories:
# expalin each datatypes with all function and  examples 
# srting is a data type   the defination of string is
# A string in Python is a sequence of characters.
#  It is a derived data type. Strings are immutable.
#  This means that once defined, they cannot be changed.
#  Many Python methods, such as replace(), join(), or split() modify strings.
#  However, they do not modify the original string.
#  They create a copy of a string which they modify and return to the caller.
#  Strings are defined either with a single quote or a double quotes.
#  You can display a string literal with the print() function:
# Example
# Strings in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".
# You can display a string literal with the print() function:
# Example
# print("Hello")
# print('Hello')
# Strings can be assigned to variables
# Example
# a = "Hello"
# print(a)
# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:
# Example
# You can use three double quotes:
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)
# Or three single quotes:   
# Example
# a = '''Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt

# ut labore et dolore magna aliqua.'''
# print(a)
# Strings are Arrays
# Like many other popular programming languages,
# strings in Python are arrays of bytes representing unicode characters.
# However, Python does not have a character data type,
# a single character is simply a string with a length of 1.
# Square brackets can be used to access elements of the string.
# Example
# Get the character at position 1 (remember that the first character has the position 0):
# a = "Hello, World!"
# print(a[1])
# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
# Example
# Get the characters from position 2 to position 5 (not included):
# b = "Hello, World!"
# print(b[2:5])
# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
# Example
# Get the characters from position 5 to position 1, starting the count from the end of the string:
# b = "Hello, World!"
# print(b[-5:-2])
# String Length
# To get the length of a string, use the len() function.
# Example
# The len() function returns the length of a string:
# a = "Hello, World!"
# print(len(a))
# String Methods
# Python has a set of built-in methods that you can use on strings.
# Note: All string methods returns new values. They do not change the original string.
# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case 
# isnumeric()	Returns True if all characters in the string are numeric    
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning
# String Literals
# String literals in python are surrounded by either single quotation marks, or double quotation marks.
# 'hello' is the same as "hello".   
# You can display a string literal with the print() function:
# Example
# print("Hello")
# print('Hello')
# Assign String to a Variable
# Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
# Example
# a = "Hello"
# print(a)
# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:
# Example
# You can use three double quotes:
a= """Lorem ipsum dolor sit amet"""
print  (a)
# Or three single quotes:
# Example

  


# Text Type:	str
# string is 



##############################################################################################################
#                                  Numeric Types:	int, float, complex 
# what is int ?
# An integer is a whole number, positive or negative,
#  without decimals, of unlimited length.
# Example
# Integers:
# x = 1
# y = 35656222554887711
# z = -3255522
# what will return  is default value of int ?
# int default value is 0 
# Example 
# x = int()
# print(x)
# integer is mutable or immutable ?
# integer is immutable
# Example
# x = 1
# print(x)
# what is biult-in function of int ?
# Built-in Functions
# The Python int() method converts the specified value into an integer number.
# The int() method returns an integer object 
# constructed from a number or string x, or return 0 if no arguments are given.
# Example
# Convert a number or string x to an integer, or return 0 if no arguments are given:
# what is syntax of int  function ?
# Syntax
# int(x=0, base=10)     # x is number or string   base is 10   default value of x is 0   
# Example   
# a=int("101101" ,2)  # 45 # "101101" is binary number and 2 is base of binary number
# x = int(1)
# y = int(2.8)
# z = int("3")
# print(x)
# print(y)
# print(z)

# Here are some of the commonly used built-in functions in Python that work with integers:

# - abs() - Returns absolute value of an integer
# example
# print(abs(-1)) # 1

# - bin() - Converts integer to binary string 
    # example 
    # print(bin(5)) # 0b101

# - divmod() - Returns quotient and remainder of integer division
    # example
    # print(divmod(9, 2)) # (4, 1)  # 9/2 = 4 remainder 1   

# - hex() - Converts integer to hexadecimal string
    # example   
    # print(hex(255)) # 0xff


# - int() - Converts string/float to integer
    # example 
    # print(int("10")) # 10

# - max() - Returns largest of given integers
    # example
    # print(max(1, 2, 3)) # 3

# - min() - Returns smallest of given integers
    # example
    # print(min(1, 2, 3)) # 1
# - oct() - Converts integer to octal string
    # example
    # print(oct(8)) # 0o10

# - pow() - Raises integer to a power
    # example
    # print(pow(2, 3)) # 8

# - round() - Rounds floating point number to nearest integer
    # example
    # print(round(2.5)) # 3

# - sum() - Sums integers in iterable  
    # example
    # print(sum([1, 2, 3])) # 6

# Additionally, the integer class defines some useful methods: # example
    # example
    # print((1).bit_length()) # 1

# - to_bytes() - Returns integer as bytes object
        # example
        # print((1024).to_bytes(2, byteorder="big")) # b'\x04\x00'
# - bit_length() - Returns number of bits to represent integer  # example
        # example
        # print((1024).bit_length()) # 11

# - bit_count() - Counts number of 1 bits in binary representation 
        # example 
        # print((10).bit_count()) # 2
# - from_bytes() - Creates integer from bytes object
        # example
        # print((b'\x00\x10').from_bytes(byteorder="big")) # 16
# There are also built-in functions that convert integers to different number types:

# - float() - Creates a float from an integer

# - complex() - Creates complex number with imaginary part as 0

# - bool() - Creates False for 0, True for all other integers

# And some math-related built-in functions: 

# - pow() - Raises integer to power
# -dir() - Returns list of attributes and methods of integer
# example
# print(dir(1)) # ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
# help() - Returns help string for integer class
# example
# print(help(1)) # Help on int object:  (etc)
# id() - Returns unique integer identifier for integer
# example
# print(id(1)) # 140735674176640
# isinstance() - Returns True if object is an integer
# example
# print(isinstance(1, int)) # True
# print(isinstance(1.0, int)) # False
# isobject() - Returns True if object is an integer 
# example
# print(isobject(1)) # True 
# print(isobject(1.0)) # False
# print(isobject("1")) # False
# print(isobject(True)) # False
# type() - Returns type of object
# example
# print(type(1)) # <class 'int'>
# There are also some built-in functions that work with integers and other number types:

# - abs() - Absolute value 

# - round() - Rounds floating point to nearest integer

# - divmod() - Quotient and remainder of division

# So in summary, Python provides many built-in options for working with integers
#  like conversion, math operations, bit manipulation, etc.
#  You can find more details about these functions in the Python documentation.
#  In the next lesson, we'll look at floating point numbers.
#  See you soon!

##############################################################################################################


# what is float ?
# Float, or "floating point number" is a number, positive or negative,
# containing one or more decimals.
# Example
# Floats:
# x = 1.10
# y = 1.0
# z = -35.59
# Float can also be scientific numbers with an "e" to indicate the power of 10.
# Example
# Floats:
# x = 35e3
# y = 12E4
# z = -87.7e100
# Float default value is 0.0
# Example
# x = float()
# print(x)
# float is mutable or immutable ?
# float is immutable
# Example
# x = 1.10
# print(x)
# what is biult-in function of float ?
# Built-in Functions
# The Python float() method converts the specified value into a floating point number.
# The float() method returns a floating point number from a number or a string.
# Example
# Convert a number or string x to a floating point number, or return 0.0 if no arguments are given:
# what is syntax of float  function ?
# Syntax
# float(x) # x is number or string   base is 10   default value of x is 0
# Example
# x = float(1)
# y = float(2.8)
# z = float("3")
# w = float("4.2")
# print(x)
# print(y)
# print(z)
# print(w)
# what is complex ?
# Complex numbers are written with a "j" as the imaginary part:
# Example
# Complex:
# x = 3+5j
# y = 5j
# z = -5j
# complex default value is 0j
# Example
# x = complex()
# print(x)
# complex is mutable or immutable ? 
# complex is immutable
# Example
# x = 3+5j
# print(x)
# what is biult-in function of complex ?
# Built-in Functions
# The Python complex() method returns a complex number when real and imaginary parts are provided,
# or it converts a string to a complex number.
# The complex() method returns a complex number 
# with the value real + imag*1j or converts a string or number to a complex number.
# If the first parameter passed to this method is a string,
# it will be interpreted as a complex number and the function must be called without a second parameter.
# The complex() method returns:
# A complex number with real part real, 
# and imaginary part imag. imag defaults to zero.
# A complex number with real part real,
# and imaginary part imag. imag defaults to zero.
# Example
# Convert two strings into a complex number:
# what is syntax of complex  function ?
# Syntax
# complex(real, imag) # real is number or string   imag is number or string  default value of imag is 0
# Example
# x = complex(1, 2)
# y = complex(1)
# z = complex()
# a = complex("1")
# b = complex("1", "2")
# print(x)
# print(y)
# print(z)
# print(a)
# print(b)
# Sequence Types:	list, tuple, range

# int is 
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# Getting the Data Type 
# what is getting the data type ?

# You can get the data type of any object by using the type() function:
# Example
# Print the data type of the variable x:
x = 5
print(type(x))
# Setting the Data Type
# In Python, the data type is set when you assign a value to a variable:
# Example
# Setting the data type of a variable
x = "Hello World"	# str
x = 20	# int
x = 20.5	# float
x = 1j	# complex
x = ["apple", "banana", "cherry"]	# list
x = ("apple", "banana", "cherry")	# tuple
x = range(6)	# range
x = {"name" : "John", "age" : 36}	# dict
x = {"apple", "banana", "cherry"}	# set
x = frozenset({"apple", "banana", "cherry"})	# frozenset
x = True	# bool
x = b"Hello"	# bytes
x = bytearray(5)	# bytearray
x = memoryview(bytes(5))	# memoryview
