with open('input.txt') as file:
    input = file.read().strip().splitlines()

orda = ord('a')
ordA = ord('A')

# PART 1
sumPrio = 0

for backpack in input :
    numberOfItems = len(backpack)
    half = int(numberOfItems / 2)
    firstCompartment = backpack[0:half]
    secondCompartment = backpack[half:-1]

    wrongItem = str(set(firstCompartment).intersection(secondCompartment))[2]
    upper = wrongItem.isupper()

    priority = ord(wrongItem) - ordA + 27 if upper else ord(wrongItem) - orda + 1
    sumPrio += priority

print(sumPrio)

# PART 2
sumPrio = 0
for i in range(0, len(input), 3):
    one = input[i]
    two = input[i + 1]
    three = input[i + 2]

    badge = str(set(set(one).intersection(two)).intersection(three))[2]

    upper = badge.isupper()

    priority = ord(badge) - ordA + 27 if upper else ord(badge) - orda + 1
    sumPrio += priority

print(sumPrio)




