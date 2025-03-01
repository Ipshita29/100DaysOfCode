#Check if N is Power of 4
n=int(input())
if n <=0:
    print("False")
elif (n&(n-1))!=0:
    print("False")
elif (n-1)%3!=0:
    print("False")
else:
    print("True")