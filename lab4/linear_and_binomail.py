## Implement Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1 

#function
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search(test_list, 6)
print(f"Linear Search: Index of 6 is {result}")

## Implement Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1 

# function
test_list_sorted = sorted(test_list)
result = binary_search(test_list_sorted, 6)
print(f"Binary Search: Index of 6 in sorted list is {result}")

## Compare Performance
import time

def compare_search_algorithms(arr, target):
    # Linear Search
    start_time = time.time()
    linear_result = linear_search(arr, target)
    linear_time = time.time() - start_time
    
    # Binary Search (on sorted array)
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time
    
    print(f"Linear Search: Found at index {linear_result}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Time: {binary_time:.6f} seconds")

# Test with a larger list
large_list = list(range(10000))
compare_search_algorithms(large_list, 8888)

##  Implement Recursive Binary Search
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

# function
result = binary_search_recursive(test_list_sorted, 6, 0, len(test_list_sorted) - 1)
print(f"Recursive Binary Search: Index of 6 in sorted list is {result}")

##Create a Main Function
def main():
    # Create a list of 20 random integers between 1 and 100
    import random
    test_list = [random.randint(1, 100) for _ in range(20)]
    
    print("Original list:", test_list)
    print("Sorted list:", sorted(test_list))
    
    target = random.choice(test_list) 
    print(f"\nSearching for: {target}")
    
    # Linear Search
    result = linear_search(test_list, target)
    print(f"Linear Search: Found at index {result}")
    
    # Binary Search (iterative)
    sorted_list = sorted(test_list)
    result = binary_search(sorted_list, target)
    print(f"Binary Search (iterative): Found at index {result}")
    
    # Binary Search (recursive)
    result = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    print(f"Binary Search (recursive): Found at index {result}")
    
    # Compare performance
    print("\nPerformance Comparison:")
    compare_search_algorithms(list(range(100000)), 99999)

if __name__ == "__main__":
    main()


##############################################################
## Exercises for Students
##############################################################

#Modify the linear search function to return all indices where the target appears, not just the first one.
def linear_search(arr, target):
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices if indices else -1

# Test the modified linear_search function
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = linear_search(test_list, 6)
print(f"Linear Search: Indices of 6 are {result}")


#Implement a function that uses binary search to find the insertion point for a target value in a sorted list.

def binary_search_insertion_point(arr, target):
    ##binary_search_insertion_point that uses binary search to find the insertion point for a target value in a sorted list.
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:##The function takes two arguments: arr, which is the sorted list, and target, which is the value to be inserted into the list.
            return mid  # If target is already in the list, return its index
        elif arr[mid] < target:##Inside the loop, the function calculates the middle index mid as the average of left and right.
            left = mid + 1
        else:
            right = mid - 1
    return left  # If target is not in the list, return the index where it should be inserted

#function
test_list = [1, 3, 4, 6, 8, 10]
result = binary_search_insertion_point(test_list, 5)
print(f"Insertion Point for 5 in sorted list is {result}")

## Create a function that counts the number of comparisons made in each search algorithm.

## Implement Binary Search
def binary_search(arr, target, comparisons=0):##binary_search function implements the binary search algorithm to find the index of a target value in a sorted array. 
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
            ## If the value at index mid is less than the target value, the function updates left to mid + 1 and increments the number of comparisons.
            comparisons += 1
        else:
            right = mid - 1
            ##If the value at index mid is greater than the target value, the function updates right to mid - 1 and increments the number of comparisons.
            comparisons += 1
##  arr (the sorted array), target (the value to be searched), and comparisons (an optional argument that keeps track of the number of comparisons made during the search).
    return -1, comparisons

## Implement Linear Search
def linear_search(arr, target, comparisons=0):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        else:
            comparisons += 1
    
    return -1

## Implement a jump search algorithm and compare its performance with linear and binary search.


import time
import math

# Linear Search
def linear_search(arr, target):
    for i, item in enumerate(arr):
        if item == target:
            return i
    return -1

# Binary Search (requires a sorted array)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Jump Search (requires a sorted array)
def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    # Jump ahead in blocks of `step`
    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    # Linear search within the identified block
    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i
    return -1

# Function to test and compare the performance of each search algorithm
def compare_searches(arr, target):
    results = {}

    # Measure Linear Search time
    start_time = time.time()
    linear_search(arr, target)
    results['Linear Search'] = time.time() - start_time

    # Measure Binary Search time
    start_time = time.time()
    binary_search(arr, target)
    results['Binary Search'] = time.time() - start_time

    # Measure Jump Search time
    start_time = time.time()
    jump_search(arr, target)
    results['Jump Search'] = time.time() - start_time

    return results

# Test the functions
arr = list(range(1, 10001))  # Example array for searching
target = 9999  # Target to search for

# Compare the searches
performance = compare_searches(arr, target)
performance
