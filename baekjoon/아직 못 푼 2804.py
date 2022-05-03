"""
A, B = input().split()
index_w = 0
index_h = 0
for i in B:
    if A.find(i) != -1:
        index_w = A.find(i)
for i in A:
    if B.find(i) != -1:
        index_h = B.find(i)
for line in range(len(B)):
    if (line == index_h):
        print(A)
    else:
        print(f"{'.'*(index_w)}{B[line]}{'.'*(len(A)-(index_w+1))}")
"""

# 두 단어 A, B를 받음
A, B = input().split()

# 단어의 글자가 겹치는 위치 저장할 변수 생성
cross_index_w = 0
cross_index_h = 0

# A 안에서 B와 겹치는 글자 찾기
for letter in A:

# B의 글자와 겹치는 첫 글자의 인덱스를 저장
    if B.find(letter) != -1:
        cross_index_h = B.find(letter)
        break

# B 안에서 A와 겹치는 글자 찾기
for letter in B:

# A의 글자와 겹치는 첫 글자의 인덱스를 저장  
    if A.find(letter) != -1:
        cross_index_w = A.find(letter)
        break

# 한 줄씩 출력
for line in range(len(B)):

# 만약에 B 안에서 처음 겹치는 글자 위치의 줄이라면,
# A를 출력
    if line == cross_index_h:
        print(A)

# 이외의 경우 .을 앞뒤로 붙여 그 줄의 길이가 A 글자수만큼 되도록 만듦
    else:
        print(f"{'.'*(cross_index_w)}{B[line]}{'.'*(len(A)-(cross_index_w+1))}")