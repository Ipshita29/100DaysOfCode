#The 100 Days of Code challenge runs at Newton School of Technology (NST). Each day, two problems are released together: one in the morning and one in the evening. To win the contest, participants need to solve at least one problem each day for 100 days.
#You are given two arrays:
#• array1: Represents whether the first problem of the day has been solved (1 if solved, 0 if not solved).
#• array2: Represents whether the second problem of the day has been solved (1 if solved, 0 if not solved).
#The size of both arrays is 100, corresponding to 100 days of the contest. Your task is to determine if the participant has successfully completed the contest by solving at least one problem each day for all 100 days
arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
for i in range(100):
    if arr1[i]==0 and arr2[i]==0:
        print("False")
        break   
else:
    print("True")