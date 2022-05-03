#numbers = []
# for i in range(9):
#    numbers.append(int(input()))
#print(max(numbers), (numbers.index(max(numbers))+1), sep="\n")


"""
N = int(input())
square_list = [i * i for i in range(1, N+1)]
print(square_list)
"""
numbers = [int(input()) for i in range(9)]
print(max(numbers), (numbers.index(max(numbers))+1), sep="\n")
