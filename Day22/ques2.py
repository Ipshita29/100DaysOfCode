#Container With Most Water
def maxAmount(heights):
    l, r = 0, len(heights) - 1
    max_ar = 0
    while l < r:
        height = min(heights[l], heights[r])
        width = r - l
        max_ar = max(max_ar, height * width)
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return max_ar