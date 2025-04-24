class Edge:
    def __init__(self, first, second, weight):
        self.first = first
        self.second = second
        self.weight = weight


def find_root(parent,node):
    while parent[node] != node:
        node = parent[node]
    return node

nodes = int(input())
edges = int(input())
graph = []
for _ in range(edges):
    first, second, weight = [int(x) for x in input().split(' - ')]
    edge = Edge(first, second, weight)
    graph.append(edge)

parent = [num for num in range(nodes)]
total_cost = 0
for edge in sorted(graph, key=lambda x: x.weight):
    first_node_root = find_root(parent, edge.first)
    second_nod_root = find_root(parent, edge.second)

    if first_node_root == second_nod_root:
        continue

    parent[first_node_root] = second_nod_root
    total_cost += edge.weight

print(f'Total cost: {total_cost}')


