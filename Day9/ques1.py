#Longest Subsequence With Limited Sum
def answerQueries(nums, queries):
    nums.sort()
    res = []
    for q in queries:
        count = 0
        total = 0
        for i in nums:
            if total + i > q:
                break 
            total += i
            count += 1
        res.append(count)
    return  res

    