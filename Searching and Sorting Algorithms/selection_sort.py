numbers = [int(x) for x in input().split()]

for idx in range(0, len(numbers) - 1):
    index = numbers[idx]
    for idx2 in range(idx + 1, len(numbers)):
        if numbers[idx2] < numbers[idx]:
            numbers[idx2], numbers[idx] = numbers[idx], numbers[idx2]


print(*numbers, sep=' ')