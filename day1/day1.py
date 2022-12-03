import numpy as np

input = np.array(open("input.txt").readlines())

maxCalories = []
count = 0

for calorie in input:
    if calorie == '\n':
        maxCalories.append(count)
        count = 0
        continue
    count += int(calorie)

maxCalories.sort(reverse=True)

print(np.sum(maxCalories[0:3]))
print(maxCalories[0] + maxCalories[1] + maxCalories[2])