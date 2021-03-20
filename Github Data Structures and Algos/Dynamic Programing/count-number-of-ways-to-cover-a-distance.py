def ways(n):
    ''' 
        Same as hackerank staircase 
        https://www.geeksforgeeks.org/count-number-of-ways-to-cover-a-distance/
    '''

    if n == 1:
        return 1
    elif n ==2 :
        return  2
    elif n == 3:
        return 4 
    
    else:
        return ways(n-1) + ways(n-2) + ways(n-3)
