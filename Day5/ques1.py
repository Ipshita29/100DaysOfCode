#Sum of Odd Length Subarrays
def sumOddLengthSubarrays(arr):
    n=len(arr)
    s=0
    for i in range(n):
        req = ((i + 1) * (n - i) + 1) // 2
        s += req * arr[i]
    return s


#if we use s = req * arr[i], it will give count of odd length sumOddLengthSubarrays