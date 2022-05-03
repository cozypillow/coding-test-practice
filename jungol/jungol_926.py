"""
_ = input()
first_a = list(input().split())
first_b = list(input().split())
_ = input()
second_a = list(input().split())
second_b = list(input().split())

first_mul = list(int(first_a[i])*int(second_a[i]) for i in range(4))
second_mul = list(int(first_b[i])*int(second_b[i]) for i in range(4))
for i in first_mul:
    print(i, end=" ")
print()
for i in second_mul:
    print(i, end=" ")
"""
"""
참고 :: 2차원리스트 기본
n, m = map(int, input().split())

b = [list(map(int, input().split())) for i in range(n)]

total = 0

for i in range(n):
    for j in range(m):
        total += b[i][j]

print(total)

"""

first_array = [list(map(int, input().split())) for i in range(2)]
second_array = [list(map(int, input().split())) for i in range(2)]
for i in range(2):
    for j in range(4):
        print(first_array[i][j]*second_array[i][j],end=" ")
    print()