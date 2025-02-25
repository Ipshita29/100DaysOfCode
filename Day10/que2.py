#Pivot Index
def pivotIndex(nums):
    total = sum(nums) 
    left = 0  
    for i in range(len(nums)):  
        right = total - left - nums[i]    
        if left == right:  
            return i     
        left += nums[i]     
    return -1


    
