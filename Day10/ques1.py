#Find Smallest Letter Greater Than Target
def nextGreatestLetter(letters, y):
    lst=list(letters)
    l=0
    hi=len(lst)-1
    res=lst[0]
    while (l<=hi):
        mid = (l+hi)//2
        val = lst[mid]
        if val>y:
            res=val
            hi=mid-1
        else:
            l=mid+1
    return res