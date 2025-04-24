from collections import deque
class Edge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

def find_path(parent, node):
    result = deque()
    while node is not None:
        result.appendleft(node)
        node = parent[node]

    return result

nodes = int(input())
edges = int(input())


graph = []

for _ in range(edges):
    source, destination, weight = [int(x) for x in input().split()]
    graph.append(Edge(source, destination, weight))

start_node = int(input())
end_node = int(input())

distance = [float('inf')] * (nodes + 1)
distance[start_node] = 0
parent = [None] * (nodes + 1)

for _ in range(nodes-1):
    for edge in graph:
        if distance[edge.source] == float('inf'):
            continue
        new_distance = distance[edge.source] + edge.weight
        if new_distance < distance[edge.destination]:
            distance[edge.destination] = new_distance
            parent[edge.destination] = edge.source

for edge in graph:
    new_distance = distance[edge.source] + edge.weight
    if new_distance < distance[edge.destination]:
        print('Undefined')
        break
else:
    path = find_path(parent, end_node)
    print(*path, sep=' ')
    print(distance[end_node])




