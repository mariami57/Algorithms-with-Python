from collections import deque


class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

nodes = int(input())
edges = int(input())
graph = []

for _ in range(edges):
    start,end, weight = [int(x) for x in input().split()]
    graph.append(Edge(start,end,weight))

start_node = int(input())
end_node = int(input())

distance = [float('inf')] * (nodes + 1)
distance[start_node] = 0
parent = [None] * (nodes + 1)

for _ in range(nodes -1):
    updated = False
    for edge in graph:
        if distance[edge.start] == float('inf'):
            continue
        new_distance = distance[edge.start] + edge.weight
        if new_distance < distance[edge.end]:
            distance[edge.end] = new_distance
            parent[edge.end] = edge.start
            updated = True
    if not updated:
        break

for edge in graph:
        new_distance = distance[edge.start] + edge.weight
        if new_distance < distance[edge.end]:
            print('Negative Cycle Detected')
            break
else:
    path = deque()
    node = end_node

    while node is not None:
        path.appendleft(node)
        node = parent[node]

    print(*path, sep=' ')
    print(distance[end_node])