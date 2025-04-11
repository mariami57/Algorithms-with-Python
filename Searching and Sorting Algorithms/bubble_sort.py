numbers = [int(x) for x in input().split()]

for i in range(0, len(numbers) - 1):
    for j in range(i + 1, len(numbers)):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(*numbers, sep=' ')