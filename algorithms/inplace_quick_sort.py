

def partition(items, start, end, pivot_idx):
    low = start
    high = end - 1
    pivot_val = items[pivot_idx]
    items[pivot_idx], items[end] = items[end], items[pivot_idx]

    while low <= high:
        while items[low] < pivot_val:
            low += 1
        while items[high] >= pivot_val:
            high -= 1
        if low <= high:
            items[low], items[high] = items[high], items[low]
            low += 1
            high -= 1
    items[end], items[low] = items[low], items[end]
    return low


def quick_sort(items, start=0, end=None):

    if end is None:
        end = len(items) - 1
        pivot_idx = len(items) // 2
    else:
        pivot_idx = ((end - start) // 2) + start

    # If there is only 1 item, it's sorted
    if len(items[start:end]) <= 1:
        return items[start:end]

    # Partition items into 3 sub-lists based on the pivot
    split = partition(items, start, end, pivot_idx)
    left = quick_sort(items, start, split)
    right = quick_sort(items, split + 1, end)
    return left + items[split:split] + right

items = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
print(items)
quick_sort(items)
print(items)
