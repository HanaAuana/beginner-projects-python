
def bubble_sort(items):
    # print(items)
    swapped = True
    # Continue until we don't have to swap anymore
    last_check = len(items)
    while swapped:
        # print("{} items, checking up to {}".format(len(items), last_check))
        swapped = False
        # Loop through each pair of items in the list
        for i in range(1, last_check):
            # If the item on the left is larger, then swap the items
            if items[i - 1] > items[i]:
                items[i - 1], items[i] = items[i], items[i - 1]
                # print("Swapping {}, {}".format(items[i - 1], items[i]))
                swapped = True
                # After the final swap in the loop, we know the remaining
                # items are sorted, so we can skip them on later loops
                last_check = i
        # print(items)
    return items

items = [8, 7, 6, 5, 4, 3, 2, 1]
bubble_sort(items)
