def MergeSortRecusive(arr):
    '''
        Time complexity: O(n * log n)

    '''

    m = len(arr) // 2
    if len(arr) <= 1:
        return arr
    else:
        LS = []
        RS = []
        M = [arr[m]]
        for i in range(len(arr)):
            if i == m:
                continue
            if arr[i] > arr[m]:
                RS.append(arr[i])
            else:
                LS.append(arr[i])

        return MergeSortRecusive(LS) + M + MergeSortRecusive(RS)


# Driver Code
if __name__ == "__main__":
    arr = [i for i in range(10)]
    print(arr[::-1])
    print(MergeSortRecusive(arr[::-1] + [5]))
