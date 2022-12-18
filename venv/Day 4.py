file = open("day4.txt")
count = 0
for line in file:
    lower1,lower2,upper1,upper2,data,switch = 0,0,0,0,'',True
    for char in line:
        if char == '-':
            if switch:
                lower1 = int(data)
            else:
                lower2 = int(data)
            data = ''
            continue
        if char == ',' or char == '\n':
            if switch:
                upper1 = int(data)
                switch = False
            else:
                upper2 = int(data)
                switch = True
                break
            data = ''
            continue
        data += char
    if (lower2 <= lower1 <= upper2) or \
            (lower2 <= upper1 <= upper2) or \
            (lower1 <= lower2 <= upper1) or \
            (lower1 <= upper2 <= upper1) or \
            (lower1 <= lower2 <= upper2 <= upper1) or \
            (lower2 <= lower1 <= upper1 <= upper2):
        count += 1
print(count)