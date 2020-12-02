class Password:
    def __init__(self, min, max, letter_required, password):
        self.min = min
        self.max = max
        self.letter_required = letter_required
        self.password = password


def is_valid_part_one(pw):
    contained_count = pw.password.count(pw.letter_required)
    return contained_count >= pw.min and contained_count <= pw.max


def is_valid_part_two(pw):
    pos_one = pw.password[pw.min-1]
    pos_two = pw.password[pw.max-1]
    return (pos_one == pw.letter_required and pos_two != pw.letter_required) \
            or (pos_one != pw.letter_required and pos_two == pw.letter_required)


def main():
    input_file = "day2.input"

    passwords = []
    with open(input_file) as f:
        for line in f:
            raw = line.split()
            range = raw[0].split('-')
            min = int(range[0])
            max = int(range[1])
            letter = raw[1].rsplit(':')[0]
            password = raw[2]
            passwords.append(Password(min, max, letter, password))

    part_one_valid_passwords = [pw for pw in passwords if is_valid_part_one(pw)]
    part_two_valid_passwords = [pw for pw in passwords if is_valid_part_two(pw)]
    print(len(part_one_valid_passwords))
    print(len(part_two_valid_passwords))


if __name__ == '__main__':
    main()

