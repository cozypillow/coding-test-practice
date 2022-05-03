print("first array")
first_array = [list(map(int, input().split())) for i in range(2)]
print("second array")
second_array = [list(map(int, input().split())) for i in range(2)]
multiple_array = [[],[]]
for i in range(2):
    for j in range(3):
        multiple_array[i].append(first_array[i][j]*second_array[i][j])
for i in range(2):
    print(*multiple_array[i])
print(multiple_array)