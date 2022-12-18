file = open('day2.txt')
data, opponent, player, total_score = '', '', '', 0
         # win tie loss
outcome = ['X','Y','Z']
                # rock paper scissors
opponentchoices = ['A','B','C']

# 6 for a win
# 3 for a tie
# 1 for a loss

for line in file:
    for char in line:
        if char == ' ':
            opponent = data
            data = ''
            continue
        if char == '\n':
            round_outcome = data
            total_score += 3 * outcome.index(round_outcome)
            if round_outcome == 'Y':
                total_score += opponentchoices.index(opponent) + 1
            elif round_outcome == 'X':
                total_score += (opponentchoices.index(opponent) + 2) % 3 + 1
            else:
                total_score += (opponentchoices.index(opponent) + 1) % 3 + 1
            data = ''
            continue
        data += char

print(total_score)
file.close()