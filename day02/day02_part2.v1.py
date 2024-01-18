file = "input_part2.txt"

with open(file) as f1:
    f2 = f1.readlines()

f2 = [x.strip() for x in f2]

s = 0

for line in f2:
    if not line:
        break
    data = {"red": 0, "blue": 0, "green": 0}

    game_line = line.split(":")
    game = game_line[0].split(" ")[-1]

    sets = game_line[-1].split(";")
    sets = [x.strip() for x in sets]

    for s1 in sets:
        s1 = s1.split(",")
        s1 = [x.strip() for x in s1]

        for s2 in s1:
            n, c = s2.split(" ")
            n = int(n)
            data[c] = max(data[c], n)
    s += data["red"] * data["blue"] * data["green"]
print(s)
