#square root of a number
def integerSquareRoot(N):
    if N == 0 or N == 1:
        return N 
    lo, hi = 1, N
    ans = 0
    while lo <= hi:
        mid = (lo + hi) // 2  
        square = mid * mid 
        if square == N:
            return mid  
        elif square < N:
            ans = mid 
            lo = mid + 1 
        else:
            hi = mid - 1  
    return ans 
q = int(input()) 
for _ in range(q):
    N = int(input())
    print(integerSquareRoot(N))
