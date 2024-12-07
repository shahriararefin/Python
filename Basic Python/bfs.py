from collections import deque

def explore_park(graph, start_zone):
    # Initialize a queue for BFS and a set for visited zones
    queue = deque([start_zone])
    visited = set()
    visited_order = []
    
    while queue:
        # Pop the zone from the front of the queue
        current_zone = queue.popleft()
        
        # If the zone has already been visited, skip it
        if current_zone in visited:
            continue
        
        # Mark the zone as visited and record the visit
        visited.add(current_zone)
        visited_order.append(current_zone)
        
        # Add unvisited neighbors to the queue
        for neighbor in graph[current_zone]:
            if neighbor not in visited:
                queue.append(neighbor)
    
    return visited_order

# Define the park's graph (adjacency list representation)
park_graph = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 6],
    4: [1],
    5: [2],
    6: [3]
}

# Start exploration from Zone 0
starting_zone = 0
visit_order = explore_park(park_graph, starting_zone)
print("Order of zones visited:", visit_order)
