from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)  # For undirected graph
    
    def print_graph(self):
        for vertex in self.graph:
            print(f"{vertex}: {' '.join(map(str, self.graph[vertex]))}")
    
    # Depth-First Search (DFS)
    def dfs(self, start_vertex):
        visited = set()
        self._dfs_recursive(start_vertex, visited)
    
    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=' ')
        
        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self._dfs_recursive(neighbor, visited)
    
    # Breadth-First Search (BFS)
    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        visited.add(start_vertex)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    
    # Find all paths between two vertices
    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in self.graph:
            return []
        paths = []
        for neighbor in self.graph[start_vertex]:
            if neighbor not in path:
                new_paths = self.find_all_paths(neighbor, end_vertex, path)
                for new_path in new_paths:
                    paths.append(new_path)
        return paths
    
    # Check if the graph is connected
    def is_connected(self):
        if not self.graph:
            return True
        start_vertex = next(iter(self.graph))
        visited = set()
        self._dfs_recursive(start_vertex, visited)
        return len(visited) == len(self.graph)

# Testing Section
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 3)

    print("\n--- Graph Structure ---")
    g.print_graph()

    print("\n--- Depth-First Search (DFS) starting from vertex 0 ---")
    g.dfs(0)

    print("\n\n--- Breadth-First Search (BFS) starting from vertex 0 ---")
    g.bfs(0)

    print("\n\n--- All paths from vertex 0 to vertex 3 ---")
    all_paths = g.find_all_paths(0, 3)
    for path in all_paths:
        print(' -> '.join(map(str, path)))

    print("\n--- Is the graph connected? ---")
    print("Connected:", g.is_connected())

    # Add a disconnected vertex and test again
    g.add_vertex(4)
    print("\nAfter adding a disconnected vertex:")
    print("--- Is the graph connected? ---")
    print("Connected:", g.is_connected())

import matplotlib.pyplot as plt
import time
import random

# Optimized Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Stop if the array is already sorted
            break
    return arr

# In-place Quick Sort
def quick_sort_in_place(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    if low < high:
        pi = partition(arr, low, high)
        quick_sort_in_place(arr, low, pi - 1)
        quick_sort_in_place(arr, pi + 1, high)

# Hybrid Merge Sort with Insertion Sort for small subarrays
def insertion_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sort_hybrid(arr, threshold=10):
    if len(arr) <= 1:
        return arr
    if len(arr) <= threshold:
        insertion_sort(arr)
        return arr

    mid = len(arr) // 2
    left = merge_sort_hybrid(arr[:mid])
    right = merge_sort_hybrid(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Visualization function for sorting algorithms
def visualize_sorting_algorithm(algorithm, arr, title):
    fig, ax = plt.subplots()
    ax.set_title(title)
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")

    def update_fig(arr):
        for rect, val in zip(bar_rects, arr):
            rect.set_height(val)
        plt.pause(0.05)

    algorithm(arr, update_fig)
    plt.show()

# Sorting algorithm wrappers for visualization
def bubble_sort_visual(arr, update_fig):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
            update_fig(arr)
        if not swapped:
            break

def quick_sort_in_place_visual(arr, update_fig, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                update_fig(arr)
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        update_fig(arr)
        return i + 1

    if low < high:
        pi = partition(arr, low, high)
        quick_sort_in_place_visual(arr, update_fig, low, pi - 1)
        quick_sort_in_place_visual(arr, update_fig, pi + 1, high)

def merge_sort_hybrid_visual(arr, update_fig, threshold=10):
    if len(arr) <= 1:
        return arr
    if len(arr) <= threshold:
        insertion_sort(arr)
        update_fig(arr)
        return arr

    mid = len(arr) // 2
    left = merge_sort_hybrid_visual(arr[:mid], update_fig, threshold)
    right = merge_sort_hybrid_visual(arr[mid:], update_fig, threshold)
    merged = merge(left, right)
    for i in range(len(arr)):
        arr[i] = merged[i]
    update_fig(arr)
    return arr

# Test and visualize each sorting algorithm
test_arr = [64, 34, 25, 12, 22, 11, 90]
visualize_sorting_algorithm(bubble_sort_visual, test_arr.copy(), "Bubble Sort Visualization")
visualize_sorting_algorithm(quick_sort_in_place_visual, test_arr.copy(), "Quick Sort (In-Place) Visualization")
visualize_sorting_algorithm(merge_sort_hybrid_visual, test_arr.copy(), "Hybrid Merge Sort Visualization")

# Compare Performance
def compare_sorting_algorithms(arr):
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Quick Sort (In-Place)", quick_sort_in_place),
        ("Hybrid Merge Sort", merge_sort_hybrid)
    ]
    
    for name, func in algorithms:
        arr_copy = arr.copy()
        start_time = time.time()
        func(arr_copy)
        end_time = time.time()
        print(f"{name} took {end_time - start_time:.6f} seconds")

# Generate a large random array
large_arr = [random.randint(1, 1000) for _ in range(1000)]
# Compare the algorithms
compare_sorting_algorithms(large_arr)