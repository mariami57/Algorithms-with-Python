from collections import deque

rows = int(input())
cols = int(input())

matrix = []
sums = []

for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
    sums.append([0] * cols)

sums[0][0] = matrix[0][0]

for col in range(1, cols):
    sums[0][col] = sums[0][col-1] + matrix[0][col]

for row in range(1, rows):
    sums[row][0] = sums[row-1][0] + matrix[row][0]

for row in range(1, rows):
    for col in range(1, cols):
        sums[row][col] = max(sums[row-1][col], sums[row][col-1]) + matrix[row][col]

row = rows-1
col = cols-1
result = deque()

while row > 0 and col > 0:
    result.appendleft([row, col])

    if sums[row][col-1] >= sums[row-1][col]:
        col -= 1
    else:
        row -= 1


while row > 0:
    result.appendleft([row, col])

    row -= 1

while col > 0:
    result.appendleft([row, col])

    col -= 1

result.appendleft([0,0])

print(*result)