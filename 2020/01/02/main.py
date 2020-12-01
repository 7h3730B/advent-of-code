listOfInputs = []

with open("input.txt", "r") as inputValues:
    inputs = inputValues.read().split('\n')
    for i in inputs:
        listOfInputs.append(int(i))
        

res = [i * j * k for i in listOfInputs for j in listOfInputs for k in listOfInputs if i + j + k == 2020]
print(f'The solution is: {res[0]}')  # 173538720