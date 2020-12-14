import collections
import math
import itertools


def get_pairs(iter):
    for cur in range(0, len(iter)-1):
        yield (iter[cur], iter[cur+1])

def p1():
    input_file = "day10.input"
    with open(input_file) as f:
        adaptors = sorted([int(n) for n in f.read().split('\n') if n != ''])

    adaptors.insert(0, 0)  # the starting jolts
    adaptors.append(max(adaptors) + 3)  # our device
    diffs = collections.defaultdict(int)
    for adaptor in get_pairs(adaptors):
        diffs[adaptor[1] - adaptor[0]] += 1

    print(math.prod(diffs.values()))


def p2():
    input_file = "day10.input"
    with open(input_file) as f:
        adaptors = sorted([int(n) for n in f.read().split('\n') if n != ''])

    adaptors.insert(0, 0)  # the starting jolts
    adaptors.append(max(adaptors) + 3)  # our device

    dp = collections.Counter()
    dp[0] = 1

    # thanks to https://www.google.com/search?client=firefox-b-d&q=advent+of+code+day10+python
    for adaptor in adaptors:
        dp[adaptor] += dp[adaptor - 1] + dp[adaptor - 2] + dp[adaptor - 3]

    print(max(dp.values()))



if __name__ == '__main__':
    p1()
    p2()

