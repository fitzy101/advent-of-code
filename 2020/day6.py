from collections import Counter


def main():
    input_file = "day6.input"
    with open(input_file) as f:
        groups = [group.split() for group in f.read().split('\n\n')]

    total_unique = sum([len(set(''.join(group))) for group in groups])
    total_same = 0
    for group in groups:
        for question, count in Counter(''.join(group)).items():
            if count == len(group):
                total_same += 1

    print(total_unique)
    print(total_same)


if __name__ == '__main__':
    main()
