# CIS40: Chapter 3 Assignment: P3.4: Nandhini Pandurangan
# This program uses a function to solve problem 3.4

# P3.4: Write a program that reads three numbers and prints "all the same"
# if they are all the same, "all different" if they are all different, and "neither" otherwise

def compare_nums():
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

    # evaluating the input:
    if num1 == num2 and num2 == num3:
        print("All the same ")
    elif num1 != num2 and num2 != num3 and num1 != num3:
        print("All different")
    else:
        print("neither")

compare_nums()

''' 
Please enter 3 numbers: hello

 ----- Please enter 3 valid numbers separated by a space----- 

Please enter 3 numbers: 12 1

 ----- Please enter 3 valid numbers separated by a space----- 

Please enter 3 numbers: 1 2.0 3
All different
-------------------------------------------------------------------
Please enter 3 numbers: 2 2.0 2.0
All the same  

-------------------------------------------------------------------
Please enter 3 numbers: 10 30 10
neither

'''
