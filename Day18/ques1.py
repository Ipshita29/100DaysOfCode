#Implementing Insertion sort
def insertion_sort(seq):
    for i in range(len(seq)):
        j=i-1
        k=seq[i]
        while (j>=0) and (k<seq[j]):
            seq[j+1]=seq[j]
            j-=1
        seq[j+1]=k
    return seq

    