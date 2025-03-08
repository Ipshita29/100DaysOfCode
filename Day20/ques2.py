#Quadratic Equation Quest
k=int(input())
lo=1
hi=(int(k//2)**0.5)+1
while (lo<=hi):
    mid=(lo+hi)//2
    val=(2*mid*mid)+(5*mid)
    if val==k:
        print(int(mid))
        break
    if val < k:
        lo=mid+1
    if val > k:
        hi=mid-1
else:
    print("-1")
    