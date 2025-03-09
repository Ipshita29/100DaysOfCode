#Subset target sum (Recursion)
def f(arr, index, curr_sum, target_sum):
    if curr_sum == target_sum: 
        print("true")
        exit() 
    if index == len(arr): 
        return
    f(arr, index + 1, curr_sum + arr[index], target_sum)
    f(arr, index + 1, curr_sum, target_sum)

N = int(input())  
arr = list(map(int, input().split()))  
target_sum = int(input()) 
f(arr, 0, 0, target_sum)
print("false")