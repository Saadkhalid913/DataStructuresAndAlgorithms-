def findmin(arr):
    return minRec(arr, 0, 0, 0)
    pass


def minRec(arr, i, sum1, sum2):
    if i >= len(arr):
        return abs(sum1 - sum2)
    else:
        return min(minRec(arr, i+1, sum1 + arr[i], sum2),
                   minRec(arr, i+1, sum1, sum2 + arr[i]))

# Practice this tommorrow and look at the dynamic solution to this problem
