with open('input.txt', 'r') as f:
    entries = [line.strip() for line in f]

def get_seatid(entry):
    return int(''.join('0' if x in 'FL' else '1' for x in entry), 2)

print(max(get_seatid(entry) for entry in entries))