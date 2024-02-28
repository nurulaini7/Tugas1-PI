"""
Nama: Nurul Aini
NIM: 221402005


Question 1: Write a program using Python that reads in the user's salary and divides the number by 12 months. 
The monthly salary should be output to the console with 0 decimal places rounded up.

"""


annual_salary = float(input("Enter your annual salary: "))

monthly_salary = round(annual_salary / 12)

print(f"Your Monthly salary is: {monthly_salary}")
