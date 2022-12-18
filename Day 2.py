file = open('day2.txt')

data, opponent, player, total_score = '', '', '', 0
               # Rock paper scissors
playerchoices = ['X','Y','Z']
                # rock paper scissors
opponentchoices = ['C','A','B']

# 6 for a win
# 3 for a tie
# 0 for a loss

for line in file:
    for char in line:
        if char == ' ':
            opponent = data
            data = ''
            continue
        if char == '\n':
            player = data
            total_score += playerchoices.index(player) + 1
            data = ''
            continue
        data += char
    if playerchoices.index(player) == opponentchoices.index(opponent):
        total_score += 6
    elif (playerchoices.index(player) + 1) % 3 == opponentchoices.index(opponent):
        total_score += 3
print(total_score)
file.close()