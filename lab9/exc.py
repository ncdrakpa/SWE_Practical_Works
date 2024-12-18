
########### Exercises for Students #################

#Implement a method to find the shortest path between two vertices using BFS.
class Graph:
    # ... (previous methods remain the same)
    def find_shortest_path(self, start_vertex, end_vertex):
        if start_vertex not in self.graph or end_vertex not in self.graph:
            return "Vertices not found in the graph."
        queue = [(start_vertex, [start_vertex])]
        visited = {start_vertex: True}
        while queue:
            current_vertex, path = queue.pop(0)
            if current_vertex == end_vertex:
                return path
            for neighbor in self.graph[current_vertex]:
                if neighbor not in visited:
                    queue.append((neighbor, path + [current_vertex]))
                    visited[neighbor] = True
        return "No path found."
    
    # Test finding the shortest path
    print("\nShortest path from vertex 0 to vertex 3:")
    print(g.find_shortest_path(0, 3))

# Add a method to detect cycles in the graph.
class Graph:
    # ... (previous methods remain the same)

    def has_cycle(self):
        def _dfs(vertex):
            if vertex in visited:
                return True
            visited.add(vertex)
            for neighbor in self.graph[vertex]:
                if _dfs(neighbor):
                    return True
            visited.remove(vertex)
            return False

        visited = set()
        for vertex in self.graph:
            if _dfs(vertex):
                return True
        return False

# Test detecting cycles
print("\nDoes the graph have a cycle?", g.has_cycle())

# Implement Dijkstra's algorithm to find the shortest path in a weighted graph.
import heapq

class Graph:
    def __init__(self):
        self.graph = {}  # Dictionary to hold the graph

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))  # Add edge with weight

    def dijkstra(self, start_vertex):
        # Priority queue to hold vertices to explore
        priority_queue = []
        # Dictionary to hold the shortest path to each vertex
        shortest_paths = {vertex: float('infinity') for vertex in self.graph}
        shortest_paths[start_vertex] = 0  # Distance to the start vertex is 0
        heapq.heappush(priority_queue, (0, start_vertex))  # (distance, vertex)

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # If the distance is greater than the recorded shortest path, skip it
            if current_distance > shortest_paths[current_vertex]:
                continue

            # Explore neighbors
            for neighbor, weight in self.graph.get(current_vertex, []):
                distance = current_distance + weight

                # If a shorter path to the neighbor is found
                if distance < shortest_paths[neighbor]:
                    shortest_paths[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return shortest_paths

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1, 4)
    g.add_edge(0, 2, 1)
    g.add_edge(1, 2, 2)
    g.add_edge(1, 3, 5)
    g.add_edge(2, 1, 2)
    g.add_edge(2, 3, 8)
    g.add_edge(3, 4, 3)
    g.add_edge(4, 0, 7)

    start_vertex = 0
    shortest_paths = g.dijkstra(start_vertex)
    
    print(f"Shortest paths from vertex {start_vertex}:")
    for vertex, distance in shortest_paths.items():
        print(f"Vertex {vertex}: {distance}")

#Create a method to determine if the graph is bipartite.

class Graph:
    def __init__(self):
        self.graph = {}  # Dictionary to hold the graph

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)  # Add edge u -> v
        self.graph[v].append(u)  # Add edge v -> u (for undirected graph)

    def is_bipartite(self):
        color = {}  # Dictionary to store the color of each vertex

        for vertex in self.graph:
            if vertex not in color:  # Not yet colored
                # Start BFS from this vertex
                queue = [vertex]
                color[vertex] = 0  # Color the starting vertex with color 0

                while queue:
                    current = queue.pop(0)

                    for neighbor in self.graph[current]:
                        if neighbor not in color:  # If the neighbor is not colored
                            # Assign the opposite color
                            color[neighbor] = 1 - color[current]
                            queue.append(neighbor)
                        elif color[neighbor] == color[current]:  # If the neighbor has the same color
                            return False  # Not bipartite

        return True  # If we successfully colored the graph

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 3)
    g.add_edge(1, 2)
    g.add_edge(2, 3)

    if g.is_bipartite():
        print("The graph is bipartite.")
    else:
        print("The graph is not bipartite.")