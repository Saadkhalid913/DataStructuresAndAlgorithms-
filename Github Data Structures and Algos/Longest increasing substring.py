def LIS(arr):
    # returns length of longest increasing subsequence in the array

    if len(arr) == 1:
        return 1

    else:
        l = [1] * len(arr)

    for j in range(len(arr)):
        for i in range(j):
            if arr[i] < arr[j] and l[i] <= l[j]:
                l[j] = l[i] + 1

    return max(l)


print(LIS([1, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 8, 9]))
