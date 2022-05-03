"""
numbers = []
N = int(input())
for n in range(N):
    numbers.append(input())
numbers = sorted(numbers)
for number in numbers:
    print(int(number))
"""

numbers = []
N = int(input())
for n in range(N):
    numbers.append(int(input()))
numbers = sorted(numbers)
for number in numbers:
    print(number)