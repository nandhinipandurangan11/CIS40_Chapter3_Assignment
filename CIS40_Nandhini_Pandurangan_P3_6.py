# CIS40: Chapter 3 Assignment: P3.6 Nandhini Pandurangan
# This program uses a function to solve problem 3.6

# P3.6: Repeat Exercise P3.5, but before reading the numbers, ask the user
# whether increasing/decreasing should be "strict" or "lenient".
# In lenient mode, the sequence 3 4 4 is increasing and the sequence 4 4 4
# is both increasing and decreasing


def track_numbers2():

    # counters for while loops in input validation
    flag1 = True
    flag2 = True

    leniency = " "
    num1 = 0
    num2 = 0
    num3 = 0

    # input validation for strict/lenient
    while flag1:
        leniency = input("\nShould the increasing/decreasing of the numbers be evaluated strictly or leniently? "
                         "\nEnter strict or lenient: ").lower()

        # recalling function to make sure correct input is entered
        if leniency == "strict" or leniency == "lenient":
            flag1 = False
        else:
            print("----- Error: please enter strict or lenient ----- ")

    # input validation for 3 numbers
    while flag2:
        try:
            num1, num2, num3 = input("Please enter 3 numbers: ").split()
            num1 = float(num1)
            num2 = float(num2)
            num3 = float(num3)
            flag2 = False
        except:
            print("\n ----- Please enter 3 valid numbers separated by a space----- \n")

    # evaluating input
    if leniency == "strict":
        if num1 < num2 and num2 < num3:
            print("The numbers are in increasing order")
        elif num1 > num2 and num2 > num3:
            print("The numbers are in decreasing order")
        else:
            print("The numbers are neither increasing nor decreasing")

    if leniency == "lenient":
        if num1 <= num2 and num2 <= num3 and num1 < num3:
            print("The numbers are in increasing order")
        elif num1 >= num2 and num2 >= num3 and num1 > num3:
            print("The numbers are in decreasing order")
        else:
            print("The numbers are both increasing and decreasing")

# calling the function to solve the problem
track_numbers2()

''' 
Enter strict or lenient: lenient
Please enter 3 numbers: 3 4 4 
The numbers are in increasing order
-------------------------------------------------

Enter strict or lenient: lenient
Please enter 3 numbers: 4 4 4 
The numbers are both increasing and decreasing 

-------------------------------------------------

Enter strict or lenient: strict
Please enter 3 numbers: 3 4 4 
The numbers are neither increasing nor decreasing

-------------------------------------------------

Should the increasing/decreasing of the numbers be evaluated strictly or leniently? 
Enter strict or lenient: hello
----- Error: please enter strict or lenient ----- 

Should the increasing/decreasing of the numbers be evaluated strictly or leniently? 
Enter strict or lenient: strict
Please enter 3 numbers: abcd

 ----- Please enter 3 valid numbers separated by a space----- 

Please enter 3 numbers: 4 4 4
The numbers are neither increasing nor decreasing
'''