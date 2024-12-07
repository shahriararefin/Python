from collections import deque

def explore_park(graph, start_zone):
    queue = deque([start_zone])  # Zones to explore
    visited = set()  # Keep track of visited zones
    order = []  # Store the visit order

    while queue:
        zone = queue.popleft()  # Get the next zone
        if zone not in visited:  # Visit only if not already visited
            visited.add(zone)
            order.append(zone)
            queue.extend(graph[zone])  # Add all connected zones to the queue
    
    return order

# Define the park's connections
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
print("Order of zones visited:", explore_park(park_graph, 0))
