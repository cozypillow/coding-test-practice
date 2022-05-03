"""
N = int(input())
numbers = input()
if len(numbers)!=N:
    print("wrong input")
else:
    sum=0
    num_list=list(numbers)
    for number in num_list:
        sum+=int(number)
    print(sum)
"""
N = int(input())
numbers = input()
#if len(numbers) != N:
#    print("wrong input")
#else:
num_list = list(map(int, numbers))
print(sum(num_list))
