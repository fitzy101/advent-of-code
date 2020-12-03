import math
import sys

TREE = '#'


def count_trees(field, x_shift, y_shift):
    cur_x_pos = 0  # moving east == positive
    cur_y_pos = 0  # moving south == positive
    tree_count = 0

    while cur_y_pos < len(field):
        line = field[cur_y_pos]
        if line[cur_x_pos % len(line)] == TREE:
            tree_count += 1
        cur_y_pos += y_shift
        cur_x_pos += x_shift

    return tree_count


def main():
    args = sys.argv
    # $1 = x move
    # $2 = y move
    x_shift = int(args[1])
    y_shift = int(args[2])

    input_file = "day3.input"

    # Construct the field of trees as a list of strings.
    with open(input_file) as f:
        field = [line.strip() for line in f]

    print(count_trees(field, x_shift, y_shift))

if __name__ == '__main__':
    main()


