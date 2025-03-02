#Frog Jump - Recursion
def frogJump(heights):
    n = len(heights)
    if n == 1:
        return 0  
    dp = [0] * n  
    dp[0] = 0 
    dp[1] = abs(heights[1] - heights[0]) 
    for i in range(2, n):
        cost1 = dp[i - 1] + abs(heights[i] - heights[i - 1])
        cost2 = dp[i - 2] + abs(heights[i] - heights[i - 2])
        dp[i] = min(cost1, cost2)
    return dp[n - 1]


    