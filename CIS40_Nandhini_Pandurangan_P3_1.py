# CIS40: Chapter 3 Assignment: P3.1: Nandhini Pandurangan
# This program uses a function to solve problem 3.1

# P3.1: Write a program that reads an integer and prints whether it is negative,
# zero, or positive.


def output_sign():
    flag = True
    num = 0

    # input validation
    while flag:
        try:
            num = int(input("Please enter an integer: "))
            flag = False
        except:
            print("\n ----- Please enter a valid integer ----- \n")

    # evaluating the input and printing the result
    if num == 0:
        print("The integer is zero")
    elif num > 0:
        print("The integer is positive")
    else:
        print("The integer is negative")


# calling the function to solve the function
output_sign()

'''
Output: 

Please enter an integer: 43
The integer is positive 
------------------------------

Please enter an integer: hello

 ----- Please enter a valid integer ----- 

Please enter an integer: -34
The integer is negative
---------------------------------------

Please enter an integer: bye

 ----- Please enter a valid integer ----- 

Please enter an integer: 0
The integer is zero
'''
