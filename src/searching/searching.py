def linear_search(arr, target):
    for e in range(len(arr)):
        if arr[e] == target:
            return e

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    # first we need to sort the array
    # arr.sort()  <-- Commenting this out as it's an extra step in this case, since according to the tests, our array is sorted already

    # now we need to track the upper and lower values
    low = 0
    high = len(arr) - 1
    while low <= high:  # while we're in the range of the array/list, as it's being halved
        # we need to find the middle index point and assign that to a variable
        middle = low + high // 2    # using the floor operator to round down
        checkpoint = arr[middle]

        # Now we can check for the target:
        # If the target IS the middle, we can return it
        if checkpoint == target:
            return middle

        # is the target HIGHER than the middle? Then we need to move the low value to the middle (-1 because we already checked the middle)
        if target > checkpoint:
            low = middle - 1

        # is the target LOWER than the middle? Then we need to move the high value to the middle (+1 because we already checked the middle)
        if target < checkpoint:
            high = middle + 1

        # and this will repeat while low is < or = high, until we find our target in "middle"

    # and if we can't find the target?

    return -1  # return a not found value
