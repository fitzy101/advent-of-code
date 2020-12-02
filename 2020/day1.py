import itertools
import functools
import operator


def main():
    input_file = "day1.input"

    values = []
    with open(input_file) as f:
        values = [int(line.strip()) for line in f]

    for c in itertools.combinations(values, 2):
        if sum(c) == 2020:
            print(functools.reduce(operator.mul, c))

    for c in itertools.combinations(values, 3):
        if sum(c) == 2020:
            print(functools.reduce(operator.mul, c))


if __name__ == '__main__':
    main()
