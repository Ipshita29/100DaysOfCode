#Minimum Size Subarray Sum K
#You are given an array arr of size n, and an integer k. 
#You have to find the minimum length of a subarray of arr with sum greater than or equal to k.
def minSubArray(arr, k):
    n = len(arr)
    l = 0
    _sum = 0
    min_length = 10**9  
    for r in range(n):
        _sum += arr[r] 
        while _sum >= k:  
            min_length = min(min_length, r - l + 1)
            _sum -= arr[l]
            l += 1 
    if min_length == 10**9:
        return 0
    return min_length