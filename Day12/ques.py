#First and Last position of Key in array
def searchRange(nums, target):
    def firstoccur(nums, target):
        lo, hi = 0, len(nums) - 1
        ans = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] >= target:
                hi = mid - 1
            else:
                lo = mid + 1
            if nums[mid] == target:
                ans = mid  
        return ans

    def lastoccur(nums, target):
        lo, hi = 0, len(nums) - 1
        ans2 = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] <= target:
                lo = mid + 1
            else:
                hi = mid - 1
            if nums[mid] == target:
                ans2 = mid  
        return ans2

    ans = firstoccur(nums, target)
    ans2 = lastoccur(nums, target)
    
    return [ans, ans2]