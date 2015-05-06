

def merge_sort(items):
    if len(items) <= 1:
        return items

    # Split list into 2 roughly equal lists
    middle = len(items) // 2
    left = items[:middle]
    right = items[middle:]

    # Sort each sub-list recursively
    print("Sort: ", left, right)
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted sub-lists back together
    return merge(left, right)


def merge(left, right):
    merged = []
    l = 0
    r = 0
    # Until we exhaust one of the sub-lists
    while l < len(left) and r < len(right):
        # If the next item in the left sub-list is smaller, take that item next
        if left[l] <= right[r]:
            merged.append(left[l])
            l += 1
        # Otherwise, take the righthand item next
        else:
            merged.append(right[r])
            r += 1
    # Append any remaining items in the lefthand list
    while l < len(left):
        merged.append(left[l])
        l += 1
    # Append any remaining items in the righthand list
    while r < len(right):
        merged.append(right[r])
        r += 1
    print("Merged: ", merged)
    return merged

items = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
print(merge_sort(items))
