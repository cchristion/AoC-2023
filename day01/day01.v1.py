with open("test.txt") as file:
    file = file.readlines()

file = [x.strip() for x in file]

sum = 0

for line in file:
    for point in line:
        try:
            left = int(point)
            break
        except:
            pass
    for point in line[::-1]:
        try:
            right = int(point)
            break
        except:
            pass
    sum += int(str(left)+str(right))

print(sum)
