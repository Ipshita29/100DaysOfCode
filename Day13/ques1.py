#Print target sum subsets
ans=[]
def find_subsets(arr, target):
    return f(arr,target,0,[])

def f(arr,target,index,a):
    if index==len(arr):
        if sum(a)==target:
            global ans
            ans.append(a[:])
        return 0
    a.append(arr[index])
    f(arr,target,index+1,a)
    a.pop()
    f(arr,target,index+1,a)
    return ans


    