sheet = [[0]*100 for i in range(100)]
n = int(input())
result = 0
for _ in range(n):
    num1, num2 = map(int, input().split())
    start_point = num1
    line = 99-num2
    for i in range(10):
        for j in range(10):
            sheet[line-i][start_point+j] = 1
for line in sheet:
    result += sum(line)
print(result)

#result = sum(map(sum, sheet))
#print(result)