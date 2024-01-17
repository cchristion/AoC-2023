with open("test.txt") as file:
    file = file.readlines()

file = [x.strip() for x in file]

sum = 0

for line in file:
    for point in line:
        if point.isdigit():
            left = int(point)
            break
    for point in line[::-1]:
        if point.isdigit():
            right = int(point)
            break
    sum += int(str(left)+str(right))

print(sum)
