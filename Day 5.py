file = open('day5.txt')

stack1 = ['B','G','S','C']
stack2 = ['T','M','W','H','J','N','V','G']
stack3 = ['M','Q','S']
stack4 = ['B','S','L','T','W','N','M']
stack5 = ['J','Z','F','T','V','G','W','P']
stack6 = ['C','T','B','G','Q','H','S']
stack7 = ['T','J','P','B','W']
stack8 = ['G','D','C','Z','F','T','Q','M']
stack9 = ['N','S','H','B','P','F']
stack_container = [0,stack1,stack2,stack3,stack4,stack5,stack6,stack7,stack8,stack9]
# Swaps between 0-2 to indicate which number comes next
move_amount, from_stack, to_stack = 0,0,0

for line in file:
    data,move_from_to = '',False
    move_from_to
    for i,char in enumerate(line):
        if not char == ' ':
            data += char
            continue
        if char == ' ' and not move_from_to:
            move_amount = int(data)
            move_from_to = True
            data = ''
        elif char == ' ' and move_from_to:
            from_stack = int(data)
            data = ''
    to_stack = int(data.replace('\n',''))
    temp_stack = []
    for i in range(move_amount):
        # stack_container[to_stack].append(stack_container[from_stack].pop())
        temp_stack.append(stack_container[from_stack].pop())
    while temp_stack:
        stack_container[to_stack].append(temp_stack.pop())

for stack in stack_container:
    if not stack:
        continue
    print(stack.pop())