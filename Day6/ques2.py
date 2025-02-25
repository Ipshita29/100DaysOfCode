#Range Sum Query-3
lst=list(map(int,input().split()))
n=len(lst)
ps=[0]*(n+1)
for i in range(1,n+1):
    ps[i]=ps[i-1]+lst[i-1]  
q=int(input())
for _ in range(q):
    l,r=map(int,input().split())
    print(ps[r+1]-ps[l])

    