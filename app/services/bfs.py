from collections import deque

def bfs(graph, start_node):
    visited = []
    queue = deque([start_node])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(graph.get(node, []))  # ✅ Add connected nodes to the queue

    return visited  # ✅ Return BFS traversal order
