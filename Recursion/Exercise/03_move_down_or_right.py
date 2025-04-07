def move_down_or_right(row, col, rows, cols):
    if row >= rows or col >= cols:
        return 0
    if row == rows - 1 and col == cols - 1:
        return 1

    result = 0

    result += move_down_or_right(row, col + 1, rows, cols)
    result += move_down_or_right(row + 1, col, rows, cols)

    return result


rows = int(input())
cols = int(input())

print(move_down_or_right(0, 0, rows, cols))

