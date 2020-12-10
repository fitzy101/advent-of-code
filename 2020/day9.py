import itertools


def p1():
    input_file = "day9.input"
    with open(input_file) as f:
        numbers = [int(n) for n in f.read().split('\n') if n != '']

    pos = 0
    while any([(n[0] + n[1]) == numbers[pos+25] for n in itertools.combinations(numbers[pos:pos+25], 2)]):
        pos += 1
    else:
        invalid = numbers[pos+25]
        print(invalid)
        return invalid


def p2(invalid_number):
    input_file = "day9.input"
    with open(input_file) as f:
        numbers = [int(n) for n in f.read().split('\n') if n != '']

    for start_pos in range(0, len(numbers)):
        check_len = 2
        while check_len < len(numbers):
            nums = numbers[start_pos:check_len]
            if sum(nums) == invalid_number:
                nums = sorted(nums)
                print(nums[0] + nums[-1])
                return
            check_len += 1

if __name__ == '__main__':
    invalid = p1()
    p2(invalid)

