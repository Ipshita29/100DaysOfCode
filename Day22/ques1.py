#Find Pair with Target Sum - Hard version
def has_pair_with_sum(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo < hi:
        current_sum = arr[lo] + arr[hi]  
        if current_sum == target:
            return True
        elif current_sum < target:
            lo += 1  
        else:
            hi -= 1 
    return False