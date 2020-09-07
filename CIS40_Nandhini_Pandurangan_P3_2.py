# CIS40: Chapter 3 Assignment: P3.2: Nandhini Pandurangan
# This program uses a function to solve problem 3.2

# P3_2: Write a program that reads a floating-point number and prints "zero"
# if the number is zero. Otherwise, print "positive" or negative. Add "small"
# if the absolute value of the number is less than 1, or "large" if it exceeds 1,000,000


def output_num_info():
    flag = True
    num = 0

    # input validation
    while flag:
        try:
            num = float(input("Please enter an a floating-point number: "))
            flag = False
        except:
            print("\n ----- Please enter a valid floating-point number ----- \n")

    # evaluating the input and printing results
    if num == 0:
        print("The number is zero", end=" ")
    elif num > 0:
        print("The number is positive", end=" ")
    else:
        print("The number is negative", end=" ")

    if abs(num) < 1:
        print("and it is small")
    if abs(num) > 1000000:
        print("and it is large")


# calling the function to solve the problem
output_num_info()

'''
Output: 

Please enter an a floating-point number: hello

 ----- Please enter a valid floating-point number ----- 

Please enter an a floating-point number: 0
The number is zero and it is small
------------------------------------------------------------
Please enter an a floating-point number: -1000000
The number is negative 
------------------------------------------------------------
Please enter an a floating-point number: -1000001
The number is negative and it is large
------------------------------------------------------------
Please enter an a floating-point number: bye

 ----- Please enter a valid floating-point number ----- 

Please enter an a floating-point number: 400
The number is positive 
'''
