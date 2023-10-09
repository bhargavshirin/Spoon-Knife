def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]  # Choose a pivot element
    left = [x for x in arr if x < pivot]  # Elements less than the pivot
    middle = [x for x in arr if x == pivot]  # Elements equal to the pivot
    right = [x for x in arr if x > pivot]  # Elements greater than the pivot

    return quick_sort(left) + middle + quick_sort(right)

# Example usage:
my_list = [12, 4, 5, 6, 7, 3, 1, 15]
sorted_list = quick_sort(my_list)
print("Sorted array:", sorted_list)
