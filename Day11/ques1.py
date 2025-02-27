#Search a 2D sorted Matrix
def searchMatrix(mat, target):
    n=len(mat)
    m=len(mat[0])
    lo=0
    hi=n*m-1
    while lo <= hi:
        mid = (lo + hi) // 2
        row = mid // m
        col = mid % m 
        if mat[row][col] == target:
            return True
        elif mat[row][col] < target:
            lo = mid + 1
        else:
            hi = mid - 1   
    return False


    