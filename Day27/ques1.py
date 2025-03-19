#House of Robbers
def robfrom(nums,i):
    if i>=len(nums):
        return 0
    robthis=nums[i]+robfrom(nums,i+2)
    skipthis=robfrom(nums,i+1)
    return max(robthis,skipthis)

def rob(nums):
    return robfrom(nums,0)
    