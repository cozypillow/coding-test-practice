participants = [sum(map(int, input().split())) for _ in range(5)]
first_participant = max(participants)
print(participants.index(first_participant)+1, first_participant)