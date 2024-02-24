# # python 1st Exercise or chalanges 
# Certainly! Here are 40 challenges or problems related to numeric data types in Python, focusing on `int`, `float`, `bool`, and `complex` types. Each set contains 10 problems:

# ### Integer Challenges (int):

# 1. **Factorial Calculation:**
#    Write a function to calculate the factorial of a given integer.

# solution 1
# user_input = int(input("Enter a number to find factorial : "))
# fact = 1
# if user_input== 0 or 1:
#     print("0 and 1 factorial alwasy equal 1")
# for i in range(1, user_input+1):
#     fact = fact * i
# print(fact)

#.............................
# solution  2  
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# user_input = int(input("Enter a number to find factorial : "))
# print(factorial(user_input))
#.............................


# 2. **Prime Number Checker:**
#    Create a function to check if a given integer is a prime number.
# so first exaplain what is prime number  : prime number is  natural numbers greater than 1 
# and those numbers are only divisible by 1 and itself thats are called prime number
# example : 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37
# so we need to check the given number is divisible by 1 and itself only
# ....................................
# solution 1  
# user_input = int(input("Enter a number to check prime number : "))
# if user_input > 1:
#     for i in range(2, user_input):
#         if user_input % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")
# else:
#     print("Not a prime number")

#............................. now code visulization of prime number 
# let me explain the code
# user_input = 5  # user input
# 5 > 1 so it will go to the next line 
# for i in range(2, 5): # 2, 3, 4 
#     if 5 % 2 == 0: # 5 % 2 = 1 not equal to 0 so it will go to the next line
#     if 5 % 3 == 0: # 5 % 3 = 2 not equal to 0 so it will go to the next line
#     if 5 % 4 == 0: # 5 % 4 = 1 not equal to 0 so it will go to the next line
#     else: # so it will print prime number
# othwise it will print not a prime number of outer else condition 
# so it will print prime number
#.............................
# other example explanation
# let if user_input = 4 
# 4 > 1 so it will go to the next line
# for i in range(2, 4): # 2, 3
#     if 4 % 2 == 0: # 4 % 2 = 0 so it will print not a prime number
#     break
# so it will print not a prime number
#.............................


    
    

# 3. **Palindrome Number:**
#    Determine if a given integer is a palindrome (reads the same backward as forward).
# so first explain what is palindrome number : palindrome number is a number that remains the same when its
#  digits are reversed example 121, 12321, 123321, 1234321
# .............................................
# solution 1 with code visualization 
# user_input = int(input("Enter a number to check palindrome number : "))
# temp = user_input
# rev = 0
# while user_input > 0:
#     rem = user_input % 10
#     rev = rev * 10 + rem
#     user_input = user_input // 10
# if temp == rev:
#     print("Palindrome number")
# else:
#     print("Not a palindrome number")
#.............................................  code visualization and explanation
# let me explain the code 
# user_input = 121 # user input
# temp = 121 # temp variable for store the user input value 
# rev = 0 # rev variable for store the reverse value of user input 
# while user_input > 0: # 121 > 0 so it will go to the next line
#     rem = 121 % 10   # 121 % 10 = 1 so it will go to the next line 
#     rev = 0 * 10 + 1 # rev = 1 so it will go to the next line
#     user_input = 121 // 10 # 121 // 10 = 12 so it will go to the next line
#     rem = 12 % 10 # 12 % 10 = 2 so it will go to the next line
#     rev = 1 * 10 + 2 # rev = 12 so it will go to the next line
#     user_input = 12 // 10 # 12 // 10 = 1 so it will go to the next line
#     rem = 1 % 10 # 1 % 10 = 1 so it will go to the next line
#     rev = 12 * 10 + 1 # rev = 121 so it will go to the next line
#     user_input = 1 // 10 # 1 // 10 = 0 so it will go to the next line
# if temp == rev: # 121 == 121 so it will print palindrome number
# so it will print palindrome number
# Q&A
#  Q1 .in this code why we use temp variable because we need to compare the user input value with reverse value ?
# if we directly compare the user input value with reverse value then it will not match the value  so we use temp variable 
# for store the user input value and compare with reverse value
# Q2. why we need to rem variable in this code ?
# we need to rem variable for store the remainder value of user input and add the remainder value with rev variable 
# Q3. why we use modulas 10 for rem in this code and why we can not  use other value ?  
# we use modulas 10 for rem because we need to get the last digit of user input and add the last digit with rev variable 
# so we use modulas 10 for rem if we use other value then it will not get the last digit of user input
# Q4. why we use floor division in this code ?
# we use floor division for get the remaining value of user input and store the remaining value in user input variable
# Q5. why we use while loop in this code ?
# we use while loop for get the reverse value of user input and compare with user input value 
    
#.............................................
# 4. **Sum of Digits:**
#    Write a function to find the sum of digits of a given integer.
# so first explain what is sum of digits : sum of digits means sum of all the digits of given number is called sum of digits
# example : 123 = 1 + 2 + 3 = 6
# .............................................
# solution 1 with code visualization 
# user_input = int(input("Enter a number to find sum of digits : "))
# sum = 0
# while user_input > 0:
#     rem = user_input % 10 
#     sum = sum + rem
#     user_input = user_input // 10
# print(sum)
#.............................................  code visualization and explanation
# let me explain the code
# user_input = 123 # user input
# sum = 0 # sum variable for store the sum of digits of user input
# while user_input > 0: # 123 > 0 so it will go to the next line
#     rem = 123 % 10 # 123 % 10 = 3 so it will go to the next line
#     sum = 0 + 3 # sum = 3 so it will go to the next line
#     user_input = 123 // 10 # 123 // 10 = 12 so it will go to the next line
#     rem = 12 % 10 # 12 % 10 = 2 so it will go to the next line
#     sum = 3 + 2 # sum = 5 so it will go to the next line
#     user_input = 12 // 10 # 12 // 10 = 1 so it will go to the next line
#     rem = 1 % 10 # 1 % 10 = 1 so it will go to the next line
#     sum = 5 + 1 # sum = 6 so it will go to the next line
# print(sum) # 6 so it will print 6 as a sum of digits
# Q&A
# Q1. why we use rem variable in this code ?
# we use rem variable for store the remainder value of user input and add the remainder value with sum variable
# Q2. why we use modulas 10 for rem in this code and why we can not  use other value ?
# we use modulas 10 for rem because we need to get the last digit of user input and add the last digit with sum variable
# so we use modulas 10 for rem if we use other value then it will not get the last digit of user input
# Q3. why we use floor division in this code ?
# we use floor division for get the remaining value of user input and store the remaining value in user input variable
# Q4. why we use while loop in this code ?
# we use while loop for get the sum of digits of user input 
#.............................................


# 5. **Binary to Decimal:**
#    Convert a binary number (given as a string) to its decimal equivalent.
# so first explain what is binary number : binary number is a number that is expressed in base-2
# example : 1010, 101, 110, 111, 1001 
# .............................................
# solution 1 with code visualization
binary = input("Enter a binary number : ")
decimal = 0
for i in range(len(binary)):
    decimal = decimal + int(binary[i]) * 2 ** (len(binary) - i - 1)
print(decimal)

#.............................................  code visualization and explanation
# let me explain the code
# binary = 1010 # user input
# decimal = 0 # decimal variable for store the decimal value of binary number
# for i in range(len(binary)): # 0, 1, 2, 3
#     decimal = 0 + int(binary[0]) * 2 ** (4 - 0 - 1) # decimal = 0 + 1 * 2 ** 3 = 8 so it will go to the next line
#     decimal = 8 + int(binary[1]) * 2 ** (4 - 1 - 1) # decimal = 8 + 0 * 2 ** 2 = 8 so it will go to the next line
#     decimal = 8 + int(binary[2]) * 2 ** (4 - 2 - 1) # decimal = 8 + 1 * 2 ** 1 = 10 so it will go to the next line
#     decimal = 10 + int(binary[3]) * 2 ** (4 - 3 - 1) # decimal = 10 + 0 * 2 ** 0 = 10 so it will go to the next line
# print(decimal) # 10 so it will print 10 as a decimal value of binary number
# Q&A
# Q1. why we use for loop in this code ?
# we use for loop for get the decimal value of binary number
# Q2. why we use range(len(binary)) in this code ?
# we use range(len(binary)) for get the length of binary number and convert the binary number to decimal number
# Q3. why we use int(binary[i]) in this code ?
# we use int(binary[i]) for convert the binary number to integer value
# Q4. why we use 2 ** (len(binary) - i - 1) in this code ?
# we use 2 ** (len(binary) - i - 1) for convert the binary number to decimal number
#.............................................
 



# 6. **Common Divisor:**
#    Find the greatest common divisor (GCD) of two integers.

# 7. **Armstrong Number:**
#    Check if a given integer is an Armstrong number.

# 8. **Power of Two:**
#    Determine if a given integer is a power of two.

# 9. **Fibonacci Sequence:**
#    Generate the first N terms of the Fibonacci sequence.

# 10. **Perfect Number:**
#     Check if a given integer is a perfect number.
