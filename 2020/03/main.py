inputValues = []
x = 0
y = 0

with open('input.txt', 'r') as inputVal:
    for i in inputVal.readlines():
        inputValues.append(i.replace('\n', ''))

trees = 0
for i in inputValues:
    x += 3
    y += 1
    if x >= len(i):
        x = (x - len(i))
    if y > 322:
        print(trees) # 205
        exit(0)
    if inputValues[y][x] == '#':
        trees += 1