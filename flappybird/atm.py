"""Take a number of numbers in the list"""
n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    a = int(input("Enter a number: "))
    numbers.append(a)

numbers.sort()
print(numbers)