c = int(input())
all_case = []
for case in range(c):
    all_case.append(list(map(int, input().split())))
for case in all_case:
    avg = round((sum(case)-case[0])/case[0], 3)
    over_avg = 0
    for score in case:
        if score > avg:
            over_avg += 1
    if over_avg != 0:
        print(f"{(over_avg/(len(case)-1)*100):.3f}%")
    else:
        print("0.000%")

"""
f-string 을 사용할 수있도록 따옴표 앞에 f를 붙인 상태에서,

f'{실수:.표기할 자리수f}'
하면 거기까지 표현된다.
"""
