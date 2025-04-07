from typing import List


def nested_loops(row, idx):
    if len(row) <= idx:
        print (*row, sep=' ')
        return

    for i in range(1, len(row) + 1):
        row[idx] = i
        nested_loops(row, idx+1)

n = int(input())
row = [None] * n

nested_loops(row, 0)