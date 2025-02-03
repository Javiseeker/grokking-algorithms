from collections import deque
# Find the length of the shortest path from “cab” to “bat”.

def bfs_shortest_path(graph, start, target):
    queue = deque([[start]])
    visited = set([start])  # Add visited set to avoid cycles

    while queue:
        current_path = queue.popleft()
        current_node = current_path[-1]
        print(f"current path: {current_path}")
        print(f"current node: {current_node}")

        if current_node == target:
            return current_path

        for neighbor in graph[current_node]:
            if neighbor not in visited:  # Only explore unvisited nodes
                visited.add(neighbor)
                new_path = current_path.copy()  # Create a new path for each neighbor
                new_path.append(neighbor)
                queue.append(new_path)
    return None

# Test
graph = {
    'CAB': ['CAT','CAR'],
    'CAR': ['CAT', 'BAR'],
    'CAT': ['MAT','BAT'],
    'MAT': [],
    'BAR': ['BAT'],
    'BAT': []
}

print(bfs_shortest_path(graph, 'CAB', 'BAT'))