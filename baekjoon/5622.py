word = list(input())
time = 0

dial = {
    3: ["A", "B", "C"], 4: ["D", "E", "F"], 5: ["G", "H", "I"],
    6: ["J", "K", "L"], 7: ["M", "N", "O"], 8: ["P", "Q", "R", "S"],
    9: ["T", "U", "V"], 10: ["W", "X", "Y", "Z"]
}

for letter in word:
    for sec, letters in dial.items():
        if letter in dial[sec]:
            time+=sec

print(time)