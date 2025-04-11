def quicksort(start, end, numbers):
    if start >= end:
        return

    pivot, left, right = start, start+1, end

    while left <= right:
        if numbers[left] > numbers[pivot] > numbers[right]:
            numbers[left], numbers[right] = numbers[right], numbers[left]
        if numbers[left] <= numbers[pivot]:
            left += 1
        if numbers[right] >= numbers[pivot]:
            right -= 1

    numbers[pivot], numbers[right] = numbers[right], numbers[pivot]
    quicksort(start, right-1, numbers)
    quicksort( right+1, end, numbers)

numbers = [int(x) for x in input().split()]
quicksort(0, len(numbers)-1, numbers)

print(*numbers, sep=' ')