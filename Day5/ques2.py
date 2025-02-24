#Implementing Bubble Sort
def bubbleSort(seq):
    n=len(seq)
    for i in range(n):
        for j in range(n-i-1):
            if seq[j]>seq[j+1]:
                seq[j],seq[j+1]=seq[j+1],seq[j]
    return seq

    