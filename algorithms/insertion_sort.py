
def insertion_sort(items):
    # print(items)
    size = len(items)
    # Loop over each position in the items
    for i in range(size):
        this_item = items[i]
        next_pos = i
        # Check item against each previous item, until we reach the first item
        while next_pos > 0 and items[next_pos - 1] > this_item:
            # Shift the previous item "up" one position
            items[next_pos] = items[next_pos - 1]
            next_pos -= 1
        # Once we find the right position, insert the current item into
        items[next_pos] = this_item
        # print(items)
    return items

items = [8, 5, 2, 6, 9, 3, 1, 4, 0, 7]
insertion_sort(items)
