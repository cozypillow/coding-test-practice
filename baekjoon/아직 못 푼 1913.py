# N*N 평면 생성
N = int(input())
sheet = [[0] * N for _ in range(N)]

# 진행방향을 결정할 변수.
up_and_down = 0
left_and_right = 0

# 현재 위치의 인덱스. 처음은 중간인데 홀수니까 n//2+1
x = n//2+1
y = n//2+1

# 현재 입력중인 숫자
number = 1

# number가 n**2가 될 때까지 반복
while number != n**2+1:
#1 ~ N-1회 연속입력을 방향바꿔가며
    for i in range(1,N):
        for j in range(i):
            sheet[y][x].append(number)
            number += 1
            y+1

0,0 

0,1 

1,0 

0,-1 
0,-1

-1,0
-1,0

0,1
0,1
0,1

1,0
1,0
1,0

0,-1
0,-1
0,-1
0,-1

-1,0
-1,0
-1,0
-1,0

0,1
0,1
0,1
0,1



#for line in sheet:
#    print(line)