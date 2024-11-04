# Implement Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(test_arr.copy())
print("Bubble Sort Result:", sorted_arr)

#Implement Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
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

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(test_arr)
print("Merge Sort Result:", sorted_arr)

# Implement Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(test_arr)
print("Quick Sort Result:", sorted_arr)

# Compare Performance
import time
import random

def compare_sorting_algorithms(arr):
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort)
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

##### Exercises for Students #####

#1. Implement an in-place version of Quick Sort to improve its space efficiency

def quick_sort_inplace(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort_inplace(less) + [pivot] + quick_sort_inplace(greater)


#2.Modify Bubble Sort to stop early if the list becomes sorted before all passes are complete.

def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no elements were swapped in the inner loop, the list is already sorted
        if not swapped:
            break
    return arr

#3. Implement a hybrid sorting algorithm that uses Insertion Sort for small subarrays in Merge Sort or Quick Sort.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quick_sort_hybrid(arr, threshold=10):
    if len(arr) <= 1:
        return arr
    elif len(arr) <= threshold:
        insertion_sort(arr)
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort_hybrid(less) + [pivot] + quick_sort_hybrid(greater)

def merge_sort_hybrid(arr, threshold=10):
    if len(arr) <= 1:
        return arr
    elif len(arr) <= threshold:
        insertion_sort(arr)
        return arr
    else:
        mid = len(arr) // 2
        left = merge_sort_hybrid(arr[:mid], threshold)
        right = merge_sort_hybrid(arr[mid:], threshold)
        return merge(left, right)
    
#4. Create a visualization of how each sorting algorithm works using a library like Matplotlib
import matplotlib.pyplot as plt
import numpy as np

# Bubble Sort Visualization
def bubble_sort_visualization(arr):
    sorted_arr = arr.copy()
    sorted_indices = [i for i in range(len(arr))]
    fig, ax = plt.subplots()
    ax.plot(sorted_indices, sorted_arr, marker='o', linestyle='-')
    ax.set_title('Bubble Sort Visualization')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_xticks(sorted_indices)
    ax.set_yticks(sorted_arr)
    ax.grid(True)
    ax.set_aspect('equal', adjustable='box')

    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]
                sorted_indices[j], sorted_indices[j + 1] = sorted_indices[j + 1], sorted_indices[j]
                ax.clear()
                ax.plot(sorted_indices, sorted_arr, marker='o', linestyle='-')
                ax.set_xticks(sorted_indices)
                ax.set_yticks(sorted_arr)
                ax.grid(True)
                ax.set_aspect('equal', adjustable='box')
                plt.pause(0.01)

    plt.show()

# Merge Sort Visualization
def merge_sort_visualization(arr):
    sorted_arr = arr.copy()
    sorted_indices = [i for i in range(len(arr))]
    fig, ax = plt.subplots()
    ax.plot(sorted_indices, sorted_arr, marker='o', linestyle='-')
    ax.set_title('Merge Sort Visualization')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_xticks(sorted_indices)
    ax.set_yticks(sorted_arr)
    ax.grid(True)
    ax.set_aspect('equal', adjustable='box')

    def merge_visualization(left, right, merged):
        ax.clear()
        ax.plot(sorted_indices[left:left + len(left)], sorted_arr[left:left + len(left)], marker='o', linestyle='-', color='blue')
        ax.plot(sorted_indices[right:right + len(right)], sorted_arr[right:right + len(right)], marker='o', linestyle='-', color='red')
        ax.plot(sorted_indices[merged:merged + len(merged)], sorted_arr[merged:merged + len(merged)], marker='o', linestyle='-', color='green')
        ax.set_xticks(sorted_indices)
        ax.set_yticks(sorted_arr)
        ax.grid(True)
        ax.set_aspect('equal', adjustable='box')
        plt.pause(0.01)

    def merge_sort_visualization_helper(left, right):
        if len(left) == 0 or len(right) == 0:
            merge_visualization(left, right, sorted_indices[left:left + len(left)])
            return
        mid = len(left) // 2
        merge_sort_visualization_helper(left[:mid], left[mid:])
        merge_sort_visualization_helper(right[:mid], right[mid:])
        merge_visualization(left[:mid], right[:mid], sorted_indices[left:left + len(left)])

    merge_sort_visualization_helper(0, len(arr))

# Quick Sort Visualization
def quick_sort_visualization(arr):
    sorted_arr = arr.copy()
    sorted_indices = [i for i in range(len(arr))]
    fig, ax = plt.subplots()
    ax.plot(sorted_indices, sorted_arr, marker='o', linestyle='-')
    ax.set_title('Quick Sort Visualization')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    ax.set_xticks(sorted_indices)
    ax.set_yticks(sorted_arr)
    ax.grid(True)
    ax.set_aspect('equal', adjustable='box')

    def partition_visualization(left, right):
        ax.clear()
        ax.plot(sorted_indices[left:left + len(left)], sorted_arr[left:left + len(left)], marker='o', linestyle='-', color='blue')
        ax.plot(sorted_indices[right:right + len(right)], sorted_arr[right:right + len(right)], marker='o', linestyle='-', color='red')
        pivot_index = sorted_indices[right - 1]
        pivot_value = sorted_arr[right - 1]
        ax.plot([pivot_index, pivot_index], [0, sorted_arr[right - 1]], marker='^', linestyle='-', color='black')
        ax.set_xticks(sorted_indices)
        ax.set_yticks(sorted_arr)
        ax.grid(True)
        ax.set_aspect('equal', adjustable='box')
        plt.pause(0.01)

    def quick_sort_visualization_helper(left, right):
        if left >= right:
            partition_visualization(left, right)
            return
        pivot_index = sorted_indices[right - 1]
        pivot_value = sorted_arr[right - 1]
        j = left
        for i in range(left, right):
            if sorted_arr[i] <= pivot_value:
                sorted_indices[j], sorted_indices[i] = sorted_indices[i], sorted_indices[j]
                sorted_arr[j], sorted_arr[i] = sorted_arr[i], sorted_arr[j]
                j += 1
        sorted_indices[j], sorted_indices[right - 1] = sorted_indices[right - 1], sorted_indices[j]
        sorted_arr[j], sorted_arr[right - 1] = sorted_arr[right - 1], sorted_arr[j]
        partition_visualization(left, j)
        quick_sort_visualization_helper(left, j)
        quick_sort_visualization_helper(j + 1, right)

    quick_sort_visualization_helper(0, len(arr))

# Test the functions
test_arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort_visualization(test_arr)
merge_sort_visualization(test_arr)
quick_sort_visualization(test_arr)