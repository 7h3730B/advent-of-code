listOfInputs = []

with open("input.txt", "r") as inputValues:
    listOfInputs = inputValues.read().split('\n')

solutions = 0

for i in listOfInputs:
    splitted = i.split(':')
    numbers = splitted[0].split(' ')[0].split('-')
    firstPosition, secondPosition, letter = int(numbers[0]), int(numbers[1]), splitted[0].split(' ')[-1]
    if (splitted[-1][firstPosition] == letter and splitted[-1][secondPosition] != letter) or (splitted[-1][firstPosition] != letter and splitted[-1][secondPosition] == letter):
        solutions += 1
print(solutions) # 294