chess_plate = [list(input()) for i in range(8)]
white_space = 0
for line in range(len(chess_plate)):
    if line % 2 == 0:
        for space in range(8):
            if space % 2 == 0:
                if chess_plate[line][space]=='F':
                    white_space += 1
    else:
        for space in range(8):
            if space % 2 != 0:
                if chess_plate[line][space]=='F':
                    white_space += 1
#print(chess_plate)
print(white_space)