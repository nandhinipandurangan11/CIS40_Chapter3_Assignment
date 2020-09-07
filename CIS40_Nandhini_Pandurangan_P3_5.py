# CIS40: Chapter 3 Assignment: P3.5 Nandhini Pandurangan
# This program uses a function to solve problem 3.5

# P3.5: Write a program that reads three numbers and prints "increasing"
# if they are in increasing order, "decreasing" if they are in decreasing order
# and neither otherwise. Here, "increasing" means strictly increasing,
# with each value larger than its predecessor


def track_numbers():
    flag = True
    num1 = 0
    num2 = 0
    num3 = 0

    # input validation
    while flag:
        try:
            num1, num2, num3 = input("Please enter 3 numbers: ").split()
            num1 = float(num1)
            num2 = float(num2)
            num3 = float(num3)

            flag = False
        except:
            print("\n ----- Please enter 3 valid numbers separated by a space----- \n")

    # evaluating input
    if num1 < num2 and num2 < num3:
        print("The numbers are in increasing order")
    elif num1 > num2 and num2 > num3:
        print("The numbers are in decreasing order")
    else:
        print("The numbers are neither increasing nor decreasing")


# calling the function to solve the problem
track_numbers()

''' 
Output: 
Please enter 3 numbers: 1 2 3
The numbers are in increasing order
---------------------------------------

Please enter 3 numbers: 100 10 0
The numbers are in decreasing order
---------------------------------------

Please enter 3 numbers: 2 3 2
The numbers are neither increasing nor decreasing
'''
