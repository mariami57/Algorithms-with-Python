def reverse_array(idx, some_array):

    if idx == len(some_array) // 2:
        return

    right_idx = len(some_array) - 1 - idx
    some_array[idx], some_array[right_idx] = some_array[right_idx], some_array[idx]
    reverse_array(idx + 1,some_array)



some_array = input().split()

reverse_array(0,some_array)

print(' '.join(some_array))