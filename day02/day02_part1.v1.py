def get_line(file):
    with open(file) as f:
        for line in f:
            yield line.strip()


file = "input_part1.txt"
sum = 0
color = {"red": 12, "green": 13, "blue": 14}
for line in get_line(file):
    if not line:
        continue

    split1 = line.split(":")
    key = int(split1[0].split()[-1])

    sets = split1[-1].split(";")
    sets = [x.strip() for x in sets]
    # print(f"\n\n{key}")

    for s in sets:
        tea = False
        dice = s.split(",")
        dice = [x.strip() for x in dice]

        for q in dice:
            n, c = q.split()
            n = int(n)
            if n > color[c]:
                break

        if n > color[c]:
            break
        tea = True

    if tea:
        # print(line)
        sum += key

print(sum)
