import random  # Import random module for selecting random pivot

def randomized_quicksort(arr, low, high):
    """
    Function to sort the array using Randomized Quicksort algorithm.
    The pivot is chosen randomly from the current subarray.
    """
    if low < high:  # Only sort if there are at least two elements
        pivot_index = randomized_partition(arr, low, high)  # Get random pivot and partition
        randomized_quicksort(arr, low, pivot_index - 1)  # Sort left subarray
        randomized_quicksort(arr, pivot_index + 1, high)  # Sort right subarray

def randomized_partition(arr, low, high):
    """
    Partition the array around a random pivot. The pivot is chosen
    randomly from the subarray and moved to the end for partitioning.
    """
    random_idx = random.randint(low, high)  # Pick a random index as the pivot
    arr[high], arr[random_idx] = arr[random_idx], arr[high]  # Swap random pivot to the end
    return partition(arr, low, high)  # Partition around the pivot

def partition(arr, low, high):
    """
    Partition the array such that all elements less than or equal to the pivot
    are on the left, and all greater elements are on the right.
    """
    pivot = arr[high]  # Pivot element
    i = low - 1  # Initialize pointer for smaller elements
    for j in range(low, high):  # Traverse through subarray
        if arr[j] <= pivot:  # If element is less than or equal to pivot
            i += 1  # Move pointer
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements to maintain order
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot at the correct position
    return i + 1  # Return the pivot index

# Test randomized quicksort
arr = [3, 6, 8, 10, 1, 2, 1]
randomized_quicksort(arr, 0, len(arr) - 1)
print("Sorted Array:", arr)
