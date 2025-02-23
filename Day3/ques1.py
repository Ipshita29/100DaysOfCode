#Polycarp has a favorite sequence a[1…n] consisting of n integers. He wrote it out on the whiteboard as follow
t = int(input()) 
for _ in range(t):
    n = int(input())  
    a = list(map(int, input().split()))  
    l,r=0,n - 1
    result=[]

    while l <= r:
        if l == r:
            result.append(a[l])
        else:
            result.append(a[l])
            result.append(a[r])
        l += 1
        r -= 1
    print(*result)


    