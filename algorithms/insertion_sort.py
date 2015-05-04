
def selection_sort(items):
    # print(items)
    size = len(items)
    # Continue until we have sorted each position
    for done in range(size):
        # print("Checking last {} of {} items".format(unsorted, size))
        # Start by assuming the next item is the smallest
        smallest = done
        # Loop through all unsorted items
        for i in range(done + 1, size):
            # If an item is smaller than current smallest it's the new smallest
            if items[i] <= items[smallest]:
                smallest = i
                # print("New smallest is {} at {}".format(items[i], i))
        # If we found a different smallest item,
        # swap the smallest item into the next unsorted position
        if done != smallest:
            items[done], items[smallest] = items[smallest], items[done]
        # print(items)
    return items

items = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
selection_sort(items)
