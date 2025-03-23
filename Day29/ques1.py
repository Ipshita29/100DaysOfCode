#House Robber - II (Recursion)
# Your code here
def houseRobber(nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    def rob_helper(start, end, memo):
        if start > end:
            return 0
        if memo[start] != -1:
            return memo[start]
        memo[start] = max(nums[start] + rob_helper(start + 2, end, memo), rob_helper(start + 1, end, memo))
        return memo[start]

    memo1 = [-1] * n
    memo2 = [-1] * n

    case1 = rob_helper(0, n - 2, memo1)
    case2 = rob_helper(1, n - 1, memo2)

    return max(case1, case2)


n = int(input())
nums = list(map(int, input().split()))

print(houseRobber(nums))
