def find_all_paths(row, col, labyrinth, direction, path):
    if row < 0 or col < 0 or row >= len(labyrinth) or col >= len(labyrinth[row]):
        return


    if labyrinth[row][col] == '*':
        return

    if labyrinth[row][col] == 'v':
        return

    path.append(direction)

    if labyrinth[row][col] == 'e':
        print(''.join(path))

    else:
        labyrinth[row][col] = 'v'
        find_all_paths(row + 1, col, labyrinth, 'D', path)
        find_all_paths(row - 1, col, labyrinth, 'U', path)
        find_all_paths(row, col + 1, labyrinth, 'R', path)
        find_all_paths(row, col - 1, labyrinth, 'L', path)
        labyrinth[row][col] = '-'

    path.pop()


rows = int(input())
cols = int(input())

labyrinth = []
path = []

for _ in range(rows):
        row_data = list(input())
        labyrinth.append(row_data)

find_all_paths(0, 0, labyrinth, '', [])