#Given an integer array nums and an integer k, return the kth largest element in the array.
#Note that it is the kth largest element in the sorted order, not the kth distinct element.
def findKthLargest(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]

    