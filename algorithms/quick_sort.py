

def quick_sort(items):

    # If there is only 1 item, it's sorted
    if len(items) <= 1:
        return items

    # Pick the middle item as the pivot
    pivot = items[len(items) // 2]

    # Partition items into 3 sub-lists based on the pivot
    left = [item for item in items if item < pivot]
    middle = [item for item in items if item == pivot]
    right = [item for item in items if item > pivot]
    # print(left)
    # print(right)

    # Recursively quick_sort the left and right partitions
    left = quick_sort(left)
    right = quick_sort(right)

    # Recombine the partitions
    return left + middle + right

items = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
print(quick_sort(items))
