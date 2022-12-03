import numpy as np

input = np.genfromtxt('input.txt', dtype='str')


# PART 1
rock1 = ord('A')
rock2 = ord('X')

score = 0

for game in input:
    opponent = ord(game[0]) - rock1
    me = ord(game[1]) - rock2

    result = me - opponent

    if result == 1:
        score += 6
    elif result == 0:
        score += 3
    elif result == -2:
        score += 6

    score += me + 1

print(score)

lose = ord('X')

score = 0
# PART 2

for game in input:
    opponent = ord(game[0]) - rock1
    result = ord(game[1]) - lose - 1

    if result == 0:
        score += opponent + 1
        score += 3
    elif result == 1:
        meplay = (opponent + 1) % 3
        score += meplay + 1
        score += 6
    elif result == -1:
        meplay = (opponent - 1) % 3
        score += meplay + 1


print(score)