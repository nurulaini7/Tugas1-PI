"""
Nama : Nurul Aini
NIM : 221402005

Question 2: Write a program that reads in a whole number and divides it by 3 
and displays the result with three decimal places if they exist (rounded up)

"""



def divide_by_three_with_decimals():
    number = int(input("Enter a number: "))
    result = round(number / 3, 3)
    print("The result is:", result)

divide_by_three_with_decimals()
