#Given an array of integers nums, you start with an initial positive value startValue.
#In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
#Return the minimum positive value of startValue such that the step by step sum is never less than 1.
def minStartValue(nums):
    min_ps = 0 
    ps = 0  
    for num in nums:
        ps += num
        min_ps = min(min_ps, ps)
    return 1 - min_ps