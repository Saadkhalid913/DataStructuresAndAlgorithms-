def binarysearch(s, e, arr, tar):
    m = (s + e) // 2

    if arr[m] == tar:
        return m
    elif arr[m] < tar:
        return binarysearch(m, e, arr, tar)
    else:
        return binarysearch(s, m, arr, tar)


def binSearch(arr, tar):
    return binarysearch(0, len(arr), arr, tar)
