listOfInputs = []

with open("input.txt", "r") as inputValues:
    listOfInputs = inputValues.read().split('\n')

for i in listOfInputs:
    res = [inp for inp in listOfInputs if (2020 - int(i)) == int(inp)]
    if res != []:
        print(f'The solution is: {int(res[0]) * int(i)}') # 618144
        break