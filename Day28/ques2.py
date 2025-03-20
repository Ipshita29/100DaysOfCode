#Range_Sum using Recursion
def rangeSum(L, R):
    if L > R:
        return 0 
    if L == R:
        return L  
    return L + rangeSum(L + 1, R)