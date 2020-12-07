import re

keywords = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
kw_patt = r'(\w+):(\S+)'


def validate_passport(passport):
    if all([kw in passport for kw in keywords]):
        keys = {k:v for k, v in re.findall(kw_patt, passport)}
        valid = re.match('^\d{4}$', keys['byr']) and \
                re.match('^\d{4}$', keys['iyr']) and \
                re.match('^\d{4}$', keys['eyr']) and \
                re.match('^\d{9}$', keys['pid']) and \
                re.match('^(amb|blu|brn|gry|grn|hzl|oth)$', keys['ecl']) and \
                re.match('^#[\da-f]{6}$', keys['hcl']) and \
                re.match('^\d+(cm|in)$', keys['hgt']) and \
                int(keys['byr']) in range(1920, 2002+1) and \
                int(keys['iyr']) in range(2010, 2020+1) and \
                int(keys['eyr']) in range(2020, 2030+1)

        if 'cm' in keys['hgt']:
            valid = valid and (int(keys['hgt'].replace('cm', '')) in range(150, 193+1))
        elif 'in' in keys['hgt']:
            valid = valid and (int(keys['hgt'].replace('in', '')) in range(59, 76+1))

        return valid
    return False


def main():
    input_file = "day4.input"
    with open(input_file) as f:
        passports = [pp.replace('\n', ' ') for pp in f.read().split('\n\n')]
    print(len([pp for pp in passports if validate_passport(pp)]))


if __name__ == '__main__':
    main()

