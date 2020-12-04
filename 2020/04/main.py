def readInputs():
    with open("input.txt", "r") as inputValues:
        passports = []
        passport = []
        for i in inputValues.readlines():
            if i.strip():
                passport.append(i)
            else:
                passports.append(toDictonary(passport))
                passport = []
        return passports

def toDictonary(passport):
    tempPassport = {}
    for j in passport:
        for k in j.split(' '):
            value = k.split(':')
            tempPassport.__setitem__(value[0], value[1].replace('\n', ''))
    return tempPassport

def validatePassport(passport, neededFields):
    validFields = 8
    for i in neededFields:
        try:
            passport[i]
        except KeyError:
            validFields -= 1
            continue
    return validFields


if __name__ == '__main__':
    passports = readInputs()
    print(passports)
    neededFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    validPassports = 0
    for passport in passports:
        if validatePassport(passport, neededFields) == 8:
            validPassports += 1
    print(validPassports)  # 250
