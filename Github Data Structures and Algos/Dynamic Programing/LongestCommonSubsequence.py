def lcs(A, B):
    m = len(A)
    n = len(B)

    # we initialize an m x n matrix where the item at index [i, j] (0 <= i <= m) and (0 <= j <= n) is the value of the LCS at when
    # the string A[:i-1] is compared with the string B[ : j-1]
    memo = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            # this is a base case as either i or j being zero would result in an empty string (This is the top row and leftmost
            # column of the matrix
            if i == 0 or j == 0:
                memo[i][j] = 0
            # we subtract one as indices begin at zero, example: the first value of string A will be included for any value i > 1, therefore we
            # subtract one as the index of the first character
            elif A[i-1] == B[j-1]:
                memo[i][j] = memo[i-1][j-1] + 1
            else:
                # if the letters dont match up, the max is simply equal to the maximum of the other two cases where
                # each strings length is decremented to find the lcs of those two strings
                memo[i][j] = max(memo[i-1][j], memo[i][j-1])

                # "ag", "gxt"  ---- problem
                # "a" , "gxt"  ---- subproblem one == 0
                # "ag",  "gx"  ---- subproblem two == 1

                # proof of subproblem
                # >> "ag", "gx" --- problem
                # >> "a", "gx" = 0
                # >> "g", "gx" = 1

                # therefore, problem == 1

    # this is the final value of when the two full strings of length i and j are considered, the longest common substring
    return memo[i][j]
