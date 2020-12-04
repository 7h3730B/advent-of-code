import re

neededFields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
checks = {
    'byr': lambda x: 1920 <= int(x) <= 2002,
    'iyr': lambda x: 2010 <= int(x) <= 2020,
    'eyr': lambda x: 2020 <= int(x) <= 2030,
    'hcl': lambda x: re.match(r'#[\da-f]{6}', x) and len(x) == 7,
    'ecl': lambda x: x in eye_colors,
    'pid': lambda x: re.match(r'[0-9]{9}', x) and len(x) == 9,
    'hgt': lambda x: (x.endswith('cm') and int(x[:-2]) >= 150 and int(x[:-2]) <= 193) or (x.endswith('in') and int(x[:-2]) >= 59 and int(x[:-2]) <= 76),
    'cid': lambda x: True
}

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
            key, value = k.split(':')
            tempPassport.__setitem__(key, value.replace('\n', ''))
    return tempPassport

def passportHasAllFields(passport, neededFields):
    try:
        [passport[i] for i in neededFields]
        return True
    except:
        return False

def validatePassport(passport):
    for field in passport:
        if not checks[field](passport[field]):
            return False
    return True

if __name__ == '__main__':
    passports = readInputs()
    haveAllFields = 0
    validPassports = 0
    for passport in passports:
        if passportHasAllFields(passport, neededFields):
            haveAllFields += 1
            if validatePassport(passport):
                validPassports += 1
    print(f'{len(passports)} Passports are checked {haveAllFields} Passports have all required fields and {validPassports} Passports are valid') # 282 250 158