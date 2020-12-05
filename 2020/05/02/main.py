with open('input.txt', 'r') as f:
    entries = [line.strip() for line in f]

def getId(entry):
    return int(''.join('0' if x in 'FL' else '1' for x in entry), 2)

def getSeat(entries):
    seats = set([getId(entry) for entry in entries])
    for i in range(min(seats) + 1, max(seats)):
        if i not in seats:
            return i

print(getSeat(entries))