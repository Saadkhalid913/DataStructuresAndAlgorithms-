'''
HOURGLASS PROBLEM HACKERANK SOLUTION
'''

# initializing the 2D array
arr = []
for i in range(6):
    row = list(input().split())
    arr.append(list(map(int, row)))

# get glass function which returns the sum of values in a glass


def getglass(i, j, arr):
    toprow = [arr[i][j], arr[i][j+1], arr[i][j+2]]
    mid = arr[1+i][j+1]
    bottomrow = [arr[i+2][j], arr[i+2][j+1], arr[i+2][j+2]]

    return sum(toprow) + mid + sum(bottomrow)


# main loop vars
i = int()
j = int()
max = None
# we can only accept a max index of 3 as we add 2 to value i and j during calculations
for i in range(0, 4):
    for j in range(0, 4):
        # finding sum of glass
        val = getglass(i, j, arr)
        # checking if we need to update max
        if max == None:
            max = val
        elif val > max:
            max = val
# return
print(max)
