def mean(nums):
    sum = 0
    for n in nums:
        sum += n
    return sum / len(nums)


def median(nums):
    nums.sort()
    midpoint = int(len(nums) / 2)
    # For even number of items, we'll return two possible modes
    if len(nums) % 2 == 0:
        return nums[midpoint - 1:midpoint + 1]
    else:
        return nums[midpoint]


def mode(nums):
    counts = [[n, nums.count(n)] for n in nums]
    most = 0
    for n in counts:
        if n[1] >= most:
            most = n[1]
    candidates = []
    for n in counts:
        if n[1] >= most and n[0] not in candidates:
            candidates.append(n[0])
    if len(candidates) == 1:
        return candidates[0]
    return candidates
