def BubbleSort(arr):
    '''
        Time complexity: O(n^2)
    '''
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# Driver code
if __name__ == "__main__":
    arr = [i for i in range(10)]
    print(arr[::-1])
    print(BubbleSort(arr[:: -1]))
