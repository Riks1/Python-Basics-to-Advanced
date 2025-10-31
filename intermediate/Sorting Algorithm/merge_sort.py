"""
Merge Sort Algorithm (Divide and Conquer)

- Time Complexity: O(n log n)
- Space Complexity: O(n)
- Stable: Yes
- In-place: No (creates temporary lists)
"""

from typing import List


def merge(left: List[int], right: List[int]) -> List[int]:
    """
    Merge two sorted subarrays into one sorted list.
    
    Args:
        left: The left sorted subarray.
        right: The right sorted subarray.
    
    Returns:
        Merged sorted list containing all elements of left and right.
    """
    merged = []
    i = j = 0

    # Merge the two arrays while maintaining order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:  # Keep sorting stable
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add any remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def merge_sort(arr: List[int]) -> List[int]:
    """
    Recursively divides the array into halves, sorts them, and merges.
    
    Args:
        arr: The list of integers to be sorted.
    
    Returns:
        A new sorted list.
    """
    # Base case: A list with 0 or 1 elements is already sorted
    if len(arr) <= 1:
        return arr

    # Step 1: Divide
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Step 2: Conquer (merge the sorted halves)
    return merge(left_half, right_half)


def main():
    """
    Driver function for Merge Sort demonstration.
    """
    print("=== Merge Sort Demo ===")
    arr = list(map(int, input("Enter elements separated by spaces: ").split()))

    print(f"\nOriginal array: {arr}")
    sorted_arr = merge_sort(arr)
    print(f"Sorted array:   {sorted_arr}")


if __name__ == "__main__":
    main()

"""
Example:
    Input:
        38 27 43 3 9 82 10
    Output:
        [3, 9, 10, 27, 38, 43, 82]
"""

