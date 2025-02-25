#Max Sum Subarray of Size K
N, K = map(int, input().split())
A = list(map(int, input().split()))
current_sum = sum(A[:K])
max_sum = current_sum
for i in range(K, N):
    current_sum += A[i] - A[i - K]  
    max_sum = max(max_sum, current_sum)
print(max_sum)


