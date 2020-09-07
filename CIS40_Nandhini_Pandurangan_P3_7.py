# CIS40: Chapter 3 Assignment: P3.7 Nandhini Pandurangan
# This program uses a function to solve problem 3.7. It modifies the function used in 3.5

# P3.7: Write a program that reads in three integers and prints "in order"
# if they are sorted in ascending or descending order, or "not in order" otherwise


def track_numbers3():
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
    if (num1 < num2 and num2 < num3) or (num1 > num2 and num2 > num3):
        print("The numbers are in order")
    else:
        print("The numbers are not in order")


# calling the function to solve the problem
track_numbers3()

''' 
Output: 

Please enter 3 numbers: 1 2 5
The numbers are in order
----------------------------------

Please enter 3 numbers: 10 5 2
The numbers are in order
----------------------------------
Please enter 3 numbers: hello

 ----- Please enter 3 valid numbers separated by a space----- 

Please enter 3 numbers: 2 100 39
The numbers are not in order
'''