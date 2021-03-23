def InsertionSort(arr):
    '''
        Time Complexity: O(n^2)
    '''

    sInx = 1
    n = len(arr)
    for i in range(1, n):  # main loop
        if arr[i] < arr[i-1]:  # detecting unordered pairs
            j = 0
            temp = arr[i]
            # finding index j where the item at i can be inserted
            while j < sInx-1 and arr[j] < arr[i]:
                j += 1

            # shifting all items from j to the end of the sorted partion one index to make room for arr[i]
            arr[j+1:sInx + 1] = arr[j:sInx]
            arr[j] = temp  # assigning arr[i] to arr[j] after storing it in a temp var
            sInx += 1  # increasing size of sorted partition
        else:
            sInx += 1

    return arr


# Driver Code
if __name__ == "__main__":
    arr = [i for i in range(10)]
    print(arr[::-1])
    print(InsertionSort(arr[:: -1]))
