def add_edge(graph, u, v):
    graph[u].append(v)

def bfs(graph, start):
    visited = set([start])
    queue = [start]

    while queue:
        node = queue.pop(0)
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)

graph = {i: [] for i in range(4)}
add_edge(graph, 0, 1)
add_edge(graph, 0, 2)
add_edge(graph, 1, 2)
add_edge(graph, 2, 0)
add_edge(graph, 2, 3)
add_edge(graph, 3, 3)

print("Following is Breadth First Traversal (starting from vertex 2)")
bfs(graph, 2)