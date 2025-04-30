str1 = input()
str2 = input()

dp = []
rows = len(str1) + 1
cols = len(str2) + 1

for _ in range(len(str1)+1):
    dp.append([0] * (len(str2) + 1) )


for col in range(1, cols):
    dp[0][col] = col

for row in range(1, rows):
    dp[row][0] = row


for row in range(1, rows):
    for col in range(1, cols):
        if str1[row - 1] == str2[col - 1]:
            dp[row][col] = dp[row - 1][col - 1]
        else:
            dp[row][col] = min(dp[row][col - 1], dp[row - 1][col]) +1

print(f'Deletions and Insertions: {dp[rows-1][cols-1]}')