file = open('day3.txt')

lower_case = 'abcdefghijklmnopqrstuvwxyz'
upper_case = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
priority_sum,priority = 0,0

for line in file:
    half_length = int(len(line)/2)
    first_rucksack = set(line[:half_length])
    second_rucksack = set(line[half_length:])

    intersection = first_rucksack.intersection(second_rucksack)

    for item in intersection:
        if not lower_case.find(item) == -1:
            priority = lower_case.find(item)+1
        elif upper_case.find(item):
            priority = upper_case.find(item)+27
        priority_sum += priority
print(priority_sum)