edges = int(input())
nodes = set()

graph = []

for _ in range(edges):
    source, destination, weight_as_str = input().split()
    weight = float(weight_as_str)
    graph.append((source, destination, weight))
    nodes.add(source)
    nodes.add(destination)

start_node = input()

distance = {node: float('-inf') for node in nodes}
distance[start_node] = 1

parent = {node: None for node in nodes}

for _ in range(len(nodes)-1):
    for (source, destination, weight) in graph:
        new_distance = weight * distance[source]
        if new_distance > distance[destination]:
            distance[destination] = new_distance
            parent[destination] = source


def extract_path(node, parent):
    first_node = node
    result = [node]
    while True:
        node = parent[node]
        result.append(node)
        if node == first_node:
            break

    return result[::-1]


for (source, destination, weight) in graph:
    new_distance = weight * distance[source]
    if new_distance > distance[destination]:
        print(True)
        path = extract_path(start_node,parent)
        print(*path, sep= ' ')
        break
else:
    print(False)
    for node, price in distance.items():
        print(f'{node}: {price:.3f}')
