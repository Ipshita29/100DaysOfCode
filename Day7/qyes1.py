#Running Sum of 1D Array
def runningSum(nums):
    n=len(nums)
    ps = [0]*(n)
    for i in range(n):
        ps[i] = ps[i-1]+nums[i]
    return ps
    