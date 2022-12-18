file = open('day6.txt')
start_of_message = []
start_of_packet = []


for index_of_line,char in enumerate(file.readline()):
    if len(set(start_of_packet)) == len(start_of_packet) and len(start_of_packet) == 14:
        break
        exit()
    start_of_packet.append(char)
    if len(start_of_packet) > 14:
        start_of_packet.remove(start_of_packet[0])

print(index_of_line)