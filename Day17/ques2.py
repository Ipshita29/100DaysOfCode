#Inversions in bubble sort
def count_inversions(list_of_numbers):
    count=0
    n=len(list_of_numbers)
    for i in range(n):
        for j in range(n-i-1):
            if list_of_numbers[j]>list_of_numbers[j+1]:
                list_of_numbers[j],list_of_numbers[j+1]=list_of_numbers[j+1],list_of_numbers[j]
                count+=1
    return count


    