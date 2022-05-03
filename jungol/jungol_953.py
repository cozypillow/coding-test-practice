players_foulball = {}

players = list(input().split())

for player in players:
    if players_foulball.get(player, "unknown") == "unknown":
        players_foulball[player] = 1
    else:
        players_foulball[player] += 1

for player, foulball in players_foulball.items():
    if foulball == min(players_foulball.values()):
        print(player)

print(min(players_foulball.values()))