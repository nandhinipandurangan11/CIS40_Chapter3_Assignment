# CIS40: Chapter 3 Assignment: P3.3: Nandhini Pandurangan
# This program uses a function to solve problem 3.3

# P3.3: Write a program that reads an integer and prints how many digits
# the number has, by checking whether the number >= 10, >= 100 and so on.
# (Assume that all integers are less than 10 billion) >> 10 billion >> 10,000, 000, 000
# if the number is negative, multiply it by -1 first

# in this context, 0 has 1 digit

import math


def output_digits():
    flag = True
    num = 0

    # input validation
    while flag:
        try:
            num = abs(int(input("Please enter an integer: ")))
            flag = False
        except:
            print("\n ----- Please enter a valid integer ----- \n")

    # evaluating the input using by checking it against incrementing powers of 10
    for i in range (1, 11):
        digit_counter = math.pow(10, i)
        if num < digit_counter:
            print("The number has {0} digit(s)".format(i))
            break


# calling the function to solve the problem
output_digits()

'''
Output: 

Please enter an integer: 1000000
The number has 7 digit(s) 

-------------------------------------------------

Please enter an integer: hi

 ----- Please enter a valid integer ----- 

Please enter an integer: 2jehr3u

 ----- Please enter a valid integer ----- 

Please enter an integer: 0
The number has 1 digit(s) 
-------------------------------------------------

Please enter an integer: 321333980
The number has 9 digit(s)
'''
