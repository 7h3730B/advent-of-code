listOfInputs = []

with open("input.txt", "r") as inputValues:
    listOfInputs = inputValues.read().split('\n')

solutions = 0

for i in listOfInputs:
    splitted = i.split(':')
    numbers = splitted[0].split(' ')[0].split('-')
    minimum, maximum, letter, letterCount = int(numbers[0]), int(numbers[1]), splitted[0].split(' ')[-1], 0
    for j in splitted[1]:
        if j == letter:
            letterCount += 1
    if letterCount >= minimum and letterCount <= maximum:
        solutions += 1
print(solutions) # 465