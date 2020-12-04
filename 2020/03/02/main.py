def readInputs():
    with open('input.txt', 'r') as inputVal:
        inputValues = []
        for i in inputVal.readlines():
            inputValues.append(i.replace('\n', ''))
    return inputValues


def calcTrees(inputV, xSteps, ySteps):
    x, y, trees = 0, 0, 0
    for i in inputV:
        x += xSteps
        y += ySteps
        if x >= len(i):
            x = (x - len(i))
        if y >= len(inputV):
            return trees
        if inputV[y][x] == '#':
            trees += 1

if __name__ == '__main__':
    steps = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    inputValues = readInputs()
    trees = 1
    for i in steps:
        trees = trees * calcTrees(inputValues, i[0], i[1])
    print(trees) # 3952146825