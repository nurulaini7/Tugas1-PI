"""
Nama : Nurul Aini
NIM : 221402005

Question 4: Write a program that reads in a number and prints the sum of all values from 1 up to the number

"""


number = int(input("Enter a Number: "))
total_sum = sum(range(1, number + 1))
print(f"The Sum of All Values from 1 up to the Number {number} is: {total_sum}")
