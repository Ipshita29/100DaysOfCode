#Subarray Sum Equals Zero
def subarray_exists(arr, n):
    prefix_sum = 0
    seen_sums = set()
    for num in arr:
        prefix_sum += num
        if prefix_sum == 0 or prefix_sum in seen_sums:
            return True
        seen_sums.add(prefix_sum)
    return False
    