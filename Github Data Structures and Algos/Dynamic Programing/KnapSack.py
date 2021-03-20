## FROM GEEKS4GEEKS 

def K(V, W, C, n):
    # base case 
    if n == 0 or C == 0:
        return 0

    # if any item in the weights arr > capacity it cannot be included so we skip the index with n-1 
    if W[n-1] > C:
        return K(V, W, C, n-1)

    else:

        return max(V[n-1] + K(V, W, C-W[n-1], n-1), # case where we include the n-1 th item and remove it from the capacity 
        # (we also add the value of this item to the maximum so that it may be included in the sum)

            # case where we do not include the n-1th element in our answer 
            K(V, W, C, n-1))

