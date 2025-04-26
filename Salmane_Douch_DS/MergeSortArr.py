def merge_sort(thelist, low, high):
    if low < high:
        mid = (low + high) // 2

        # First divide the array
        merge_sort(thelist, low, mid)
        merge_sort(thelist, mid + 1, high)

        # Then merge the sorted halves
        merge(thelist, low, mid, high)


def merge(thelist, low, mid, high):
    lower_half = mid - low + 1
    upper_half = high - mid

    left = [0] * lower_half
    right = [0] * upper_half

    for i in range(lower_half):
        left[i] = thelist[low + i]
    for j in range(upper_half):
        right[j] = thelist[mid + 1 + j]

    i = 0
    j = 0
    k = low

    while i < lower_half and j < upper_half:
        if left[i] <= right[j]:
            thelist[k] = left[i]
            i += 1
        else:
            thelist[k] = right[j]
            j += 1
        k += 1

    # Copy remaining elements
    while i < lower_half:
        thelist[k] = left[i]
        i += 1
        k += 1

    while j < upper_half:
        thelist[k] = right[j]
        j += 1
        k += 1