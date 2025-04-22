def dfs(node, graph, visited, cycle):

    if node in cycle:
        raise Exception

    if node in visited:
        return


    visited.add(node)
    cycle.add(node)

    for child in graph[node]:
        dfs(child, graph, visited, cycle)

    cycle.remove(node)

line = input()
graph = {}
while line != 'End':
    start, destination = line.split('-')
    if start not in graph:
        graph[start] = []
    if destination not in graph:
        graph[destination] = []

    graph[start].append(destination)

    line = input()

try:
    visited = set()
    for node in graph:
        dfs(node, graph, visited, set())
    print('Acyclic: Yes')
except Exception:
    print('Acyclic: No')