spelled = {0:"zero", 1: "one", 2: "two", 3: "three", 4: "four", 
           5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

with open("test.txt") as file:
    file = file.readlines()

file = [x.strip() for x in file]

def get_num(line):
    lnum, rnum = None, None
    for index, char in enumerate(line):
        if char.isdigit():
            lnum = int(char)
            break
        if index > 1:
            for key in spelled:
                if spelled[key] in line[:index+1]:
                    lnum = key
                    break
        if lnum:
            break

    for index, char in enumerate(line[::-1]):
        if char.isdigit():
            rnum = int(char)
            break
        if index > 1:
            for key in spelled:
                if spelled[key] in line[-(index+1):]:
                    rnum = key
                    break
        if rnum:
            break
    if (lnum != None) and (rnum != None):
        return int(str(lnum)+str(rnum))
    else:
        return 0

sum = 0
for line in file:
    sum += get_num(line)

print(sum)
