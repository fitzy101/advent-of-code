
def get_seat_id(seat_number):
    rows = list(range(0, 128))
    columns = list(range(0, 8))

    row_chars = seat_number[:7]
    column_chars = seat_number[7:]

    splitter = lambda r, front, char : r[:int(len(r)/2)] if char == front else r[int(len(r)/2):]
    for row in row_chars:
        rows = splitter(rows, 'F', row)
    for column in column_chars:
        columns = splitter(columns, 'L', column)

    return rows[0] * 8 + columns[0]


def main():
    input_file = "day5.input"
    with open(input_file) as f:
        seat_numbers = f.read().split('\n')

    seat_ids = sorted([get_seat_id(seat) for seat in seat_numbers])
    max_id, min_id = max(seat_ids), min(seat_ids)
    print(max_id)

    # find the gap by looking at integers in range(min + 50, max)
    all_nums = range(min_id + 50, max_id)
    print([i for i in all_nums if i not in seat_ids][0])



if __name__ == '__main__':
    main()

