#Magical Array
def magicalArrays(arr):
    n = len(arr)
    count = 0
    lo = 0
    while lo < n:
        hi = lo
        while hi < n and arr[lo] == arr[hi]:
            hi += 1
        length = hi - lo
        count += (length * (length + 1)) // 2
        lo = hi
    return count