"""
Nama : Nurul Aini
NIM : 221402005

Question 3: Write a program that reads in a number and prints the either Small, Medium or Large 
depending on if the number is below 100 or above 200.

"""


def classify_number():
    number = int(input("Enter a number: "))
    if number < 100:
        classification = "Small"
    elif number > 200:
        classification = "Large"
    else:
        classification = "Medium"
    print("The number is:", classification)

classify_number()
