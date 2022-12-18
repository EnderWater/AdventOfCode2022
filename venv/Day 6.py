file = open('day6.txt')
queue = []
index_of_line = 0
for line in file:
    for char in line:
        if len(set(queue)) == len(queue) and len(queue) == 4:
            print(index_of_line)
            exit()
        queue.append(char)
        if len(queue) > 4:
            queue.remove(queue[0])
        index_of_line += 1