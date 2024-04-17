"""_summary_

   A
 / | \
B  C  D
| / \ |
E F   G

BFS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

DFS = ['A', 'B', 'E', 'C', 'F', 'D', 'G']


"""

# Example graph representation

graph = {
    "A": ["B", "C", "D"],
    "B": ["A", "E"],
    "C": ["A", "F"],
    "D": ["A", "G"],
    "E": ["B"],
    "F": ["C"],
    "G": ["D"],
}

from collections import deque


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal_order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return traversal_order


def dfs(graph, start, visited=None, traversal=None):

    if visited is None:
        visited = set()
    if traversal is None:
        traversal = []

    visited.add(start)
    traversal.append(start)

    for padosi in graph[start]:
        if padosi not in visited:
            dfs(graph, padosi, visited, traversal)

    return traversal


def dfs_iterative(graph, start):
    visited = set()
    traversal = []

    stack = [start]

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            traversal.append(node)

            stack.extend(reversed(graph[node]))

    return traversal


print("BFS Traversal Order:", bfs(graph, "A"))
print("DFS Traversal Order:", dfs(graph, "A"))
print("DFS Iterative Order:", dfs(graph, "A"))
