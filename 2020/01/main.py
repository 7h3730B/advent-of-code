listOfInputs = []

with open("input.txt", "r") as inputValues:
    listOfInputs = inputValues.read().split('\n')

res = [int(i) * int(j) for i in listOfInputs for j in listOfInputs if (2020 - int(i)) == int(j)]
print(f'The solution is: {res[0]}')  # 618144
