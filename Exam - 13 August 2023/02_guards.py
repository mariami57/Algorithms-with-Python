def dfs(node, graph, visited):
    if node in visited:
        return
    visited.add(node)

    for child in graph[node]:
        dfs(child, graph, visited)

nodes = int(input())
edges = int(input())

graph = {node: [] for node in range(1, nodes+1)}

for _ in range(edges):
    source, destination = [int(x) for x in input().split()]
    graph[source].append(destination)

start = int(input())
visited = set()



dfs(start, graph, visited)

unreachable = []

for node in graph.keys():
    if node not in visited:
        unreachable.append(node)

print(*sorted(unreachable), sep=' ')

