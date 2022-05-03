듣, 보 = map(int, (input().split()))

듣잡 = {}
듣보잡 = []

for _ in range(듣):
    듣잡[input()] = 0
for i in range(보):
    보잡 = input()
    if 보잡 in 듣잡.keys():
        듣보잡.append(보잡)

if len(듣보잡) == 0:
    print("0")
else:
    듣보잡 = sorted(듣보잡)
    print(len(듣보잡))
    for 잡 in 듣보잡:
        print(잡)
