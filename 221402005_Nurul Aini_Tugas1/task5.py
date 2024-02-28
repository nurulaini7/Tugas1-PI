"""
Nama : Nurul Aini
NIM : 221402005

Question 5: Write a program that reads in numbers until a -1 is entered and prints the sum of all numbers entered

"""

total_sum = 0

while True:
    number = int(input("Enter a number (or -1 to stop): "))
    if number == -1:
        break
    total_sum += number

print(f"Sum of all entered numbers: {total_sum}")
