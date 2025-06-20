first = input()
second = input()

rows = len(first) + 1
cols = len(second) + 1
dp = [([0]* cols) for _ in range(rows)]

for row in range(1, rows):
    for col in range(1, cols):
        if first[row-1] == second[col-1]:
            dp[row][col] = 1 + dp[row-1][col-1]
        else:
            dp[row][col] = max(dp[row-1][col], dp[row][col-1])

print(dp[rows-1][cols-1])

row = rows - 1
col = cols - 1

result = []

while row >= 0 and col >= 0:
    if first[row-1] == second[col-1]:
        result.append(first[row-1])
        row -= 1
        col -= 1

    elif dp[row-1][col] > dp[row][col-1]:
        row -=1
    else:
        col -=1

print(result)