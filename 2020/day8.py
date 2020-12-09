import collections
import re
import textwrap


def p1():
    input_file = "day8.input"
    with open(input_file) as f:
        instructions = [ins for ins in f.read().split('\n')]

    # instructions = [i for i in textwrap.dedent(
    # """
    # nop +0
    # acc +1
    # jmp +4
    # acc +3
    # jmp -3
    # acc -99
    # acc +1
    # jmp -4
    # acc +6
    # """).split('\n') if i != '']

    executed = collections.defaultdict(bool)
    accum = 0
    pos = 0

    ins_r = r'^(acc|nop|jmp)\s([\+\-])(\d+)$'

    while not executed[pos]:
        executed[pos] = True
        ins, dir, count = re.match(ins_r, instructions[pos]).groups()

        if ins == 'acc':
            if dir == '+':
                accum += int(count)
            else:
                accum -= int(count)

        elif ins == 'jmp':
            if dir == '+':
                pos += int(count)
            else:
                pos -= int(count)
            continue

        pos += 1
    print(accum)


def p2():
    input_file = "day8.input"
    with open(input_file) as f:
        instructions = [ins for ins in f.read().split('\n') if ins != '']

    # instructions = [i for i in textwrap.dedent(
    # """
    # nop +0
    # acc +1
    # jmp +4
    # acc +3
    # jmp -3
    # acc -99
    # acc +1
    # jmp -4
    # acc +6
    # """).split('\n') if i != '']

    all_jmp_indices = [i for i, x in enumerate(instructions) if 'jmp' in x]
    all_nop_indices = [i for i, x in enumerate(instructions) if 'nop' in x]
    ins_r = r'^(acc|nop|jmp)\s([\+\-])(\d+)$'

    for idx in all_jmp_indices:
        accum = 0
        pos = 0
        executed = collections.defaultdict(bool)
        new_instructions = instructions[:]
        new_instructions[idx] = new_instructions[idx].replace('jmp', 'nop')
        while pos < len(new_instructions):
            if executed[pos]:
                break
            executed[pos] = True

            ins, dir, count = re.match(ins_r, new_instructions[pos]).groups()
            if ins == 'jmp':
                if dir == '+':
                    pos += int(count)
                else:
                    pos -= int(count)
                continue

            elif ins == 'acc':
                if dir == '+':
                    accum += int(count)
                else:
                    accum -= int(count)
            pos += 1
        else:
            # will only ever hit here when we've got to the end of the
            # instructions
            print (accum)
            return

if __name__ == '__main__':
    p1()
    p2()

