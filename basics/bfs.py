from collections import deque

graph = {
    "A": ["B", "C", "D"],
    "B": ["A", "E"],
    "C": ["A", "F"],
    "D": ["A", "G"],
    "E": ["B"],
    "F": ["C"],
    "G": ["D"],
}


def bfs(graph, start):
    visited = set()
    traversal_order = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)

            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)

    return " -> ".join(traversal_order)


def dfs(graph, start visited=None, )

print(bfs(graph, "A"))
