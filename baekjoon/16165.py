n, m = map(int, input().split())
girlgroup_list = []

for i in range(n):
    team = input()
    member_number = int(input())
    members = []
    for _ in range(member_number):
        members.append(input())
    team = {"team": team,
            "member_number": member_number,
            "members": members
            }
    girlgroup_list.append(team)

for i in range(m):
    name = input()
    game_number = int(input())

    if game_number == 1:
        for girlgroup in girlgroup_list:
            for member in girlgroup["members"]:
                if name == member:
                    print(girlgroup["team"])
    else:
        for girlgroup in girlgroup_list:
            if girlgroup["team"] == name:
                print(*girlgroup["members"],sep="\n")