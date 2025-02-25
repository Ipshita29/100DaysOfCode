#Little Alice has recently started studying multiples of 5, and today he is particularly fascinated by numbers divisible by 5. 
# He has a collection of queries where each query provides a range of indices [l, r] 
# in an array of integers arr and asks him to find how many integers in that range are divisible by 5
N = int(input())  
arr = list(map(int, input().split()))  
Q = int(input())  

prefix = [0] * N

if arr[0] % 5 == 0:
    prefix[0] = 1
else:
    prefix[0] = 0

for i in range(1, N):
    if arr[i] % 5 == 0:
        prefix[i] = prefix[i - 1] + 1
    else:
        prefix[i] = prefix[i - 1]

for _ in range(Q):
    l, r = map(int, input().split())
    if l == 0:
        print(prefix[r])
    else:
        print(prefix[r] - prefix[l - 1])

        