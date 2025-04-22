from queue import PriorityQueue
from collections import deque

class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

edges = int(input())
graph = {}

for _ in range(edges):
    start, end, weight = [int(x) for x in input().split(', ')]
    if start not in graph:
        graph[start] = []
    if end not in graph:
        graph[end] = []
    graph[start].append(Edge(start,end, weight))

start_node = int(input())
end_node = int(input())

max_node = max(graph.keys())
distance = [float('inf')] * (max_node + 1)
parent = [None] * (max_node + 1)

distance[start_node] = 0

pq = PriorityQueue()
pq.put((0, start_node))

while not pq.empty():
    min_distance, node = pq.get()
    if node == end_node:
        break
    for edge in graph[node]:
       new_distance = min_distance + edge.weight
       if new_distance < distance[edge.end]:
           distance[edge.end] = new_distance
           parent[edge.end] = node
           pq.put((new_distance, edge.end))

if distance[end_node] == float('inf'):
    print('There is no such path.')
else:
    print(distance[end_node])
    path = deque()
    node = end_node
    while node is not None:
        path.appendleft(node)
        node = parent[node]
    print(*path, sep=' ')