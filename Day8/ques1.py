#Subarray Sum Divisible by K
N, K = map(int, input().split())
A = list(map(int, input().split()))
remain_c = {}
ps = 0
c = 0
for num in A:
    ps += num
    remain = ps % K
    if remain < 0:
        remain += K
    if remain in remain_c:
        c += remain_c[remain]
        remain_c[remain] += 1 
    else:
        remain_c[remain] = 1 
    if ps % K == 0:
        c += 1
print(c)

