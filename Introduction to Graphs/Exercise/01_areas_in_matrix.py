def dfs(key, row, col, matrix, visited):
    if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
        return

    if visited[row][col]:
        return

    if matrix[row][col] != key:
        return

    visited[row][col] = True

    dfs(key, row - 1, col, matrix, visited)
    dfs(key, row + 1, col, matrix, visited)
    dfs(key, row, col - 1, matrix, visited)
    dfs(key, row, col + 1, matrix, visited)


rows = int(input())
cols = int(input())

matrix = []
visited = []

for _ in range(rows):
    matrix.append(list(input()))
    visited.append([False] * cols)

areas = {}
total_areas = 0

for row in range(rows):
    for col in range(cols):
        if visited[row][col]:
            continue

        key = matrix[row][col]
        dfs(key, row, col, matrix, visited)
        if key not in areas:
            areas[key] = 1
        else:
            areas[key] += 1
        total_areas += 1

print(f"Areas: {total_areas}")
for key, count in sorted(areas.items()):
    print(f"Letter '{key}' -> {count}")