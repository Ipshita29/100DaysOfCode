#Range Frequency Queries
def numOfFreq(arr, queries):
    n = len(arr)
    ps = [{} for _ in range(n + 1)]
    for i in range(n):
        ps[i + 1] = ps[i].copy()  
        if arr[i] in ps[i + 1]:
            ps[i + 1][arr[i]] += 1
        else:
            ps[i + 1][arr[i]] = 1
    result = []
    for i, j, x in queries:
        count_j = ps[j + 1].get(x, 0)  
        count_i = ps[i].get(x, 0)      
        result.append(count_j - count_i)       

    return result

