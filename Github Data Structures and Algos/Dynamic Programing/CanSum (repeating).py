# def canSum(arr, target):
#     '''
#       Recursive
#     '''
#     if target == 0:
#         return True
#     if target < 0:
#         return False
#     return any([canSum(arr, target-i) for i in arr])


def canSum(target, arr, memo={}):
    if target < 0:
        return False
    if target == 0:
        return True
    if target in memo:
        return memo[target]
    for i in arr:
        if canSum(target - i, arr):
            return True
        else:
            memo[target - i] = canSum(target - i, arr)
    return False


print(canSum(1500, [2, 3, 4, 8]))
