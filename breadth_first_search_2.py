from collections import deque

def bfs_shortest_path(graph, start, target):
    # Initialize queue with just nodes instead of paths
    queue = deque([start])
    visited = set([start])
    # Dictionary to store parent relationships
    parent = {start: None}
    
    while queue:
        current_node = queue.popleft()
        
        if current_node == target:
            # Reconstruct path using parent dictionary
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = parent[current_node]
            return path[::-1]  # Reverse path to get start->target
            
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current_node
                queue.append(neighbor)
                
    return None  # No path found

# Test
graph = {
    'S': ['A','B'],
    'A': ['C', 'F'],
    'B': ['C','D'],
    'C': [],
    'D': ['F'],
    'F': []
}

print(bfs_shortest_path(graph, 'S', 'F'))