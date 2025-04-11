# def binary_search(numbers, target, left_index, right_index):
#
#     if left_index > right_index:
#         return -1
#
#     mid_index = (left_index + right_index) // 2
#
#     if numbers[mid_index] == target:
#         return mid_index
#
#     elif numbers[mid_index] < target:
#         return binary_search(numbers, target, mid_index + 1, right_index)
#     else:
#         return binary_search(numbers, target, left_index, mid_index - 1)
#
# numbers = [int(x) for x in input().split()]
# target = int(input())
# left_idx = 0
# right_idx = len(numbers) - 1
#
#
# print(binary_search(numbers, target, left_idx, right_idx))


def binary_search2(numbers, target):
    left_idx = 0
    right_idx = len(numbers) - 1

    while left_idx <= right_idx:
        mid_idx = (left_idx + right_idx) // 2

        if numbers[mid_idx] == target:
            return mid_idx
        elif numbers[mid_idx] > target:
            right_idx = mid_idx - 1
        else:
            left_idx = mid_idx + 1
    return -1


numbers = [int(x) for x in input().split()]
target = int(input())

print(binary_search2(numbers, target))