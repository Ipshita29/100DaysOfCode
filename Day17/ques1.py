#Sort Colors
def sortColors(nums):
    n=len(nums)
    for i in range(n):
        min_index=i
        for j in range(i+1,n):
            if nums[j]<nums[min_index]:
                min_index=j
        if i!=min_index:
            nums[i],nums[min_index]=nums[min_index],nums[i]
    return nums
    