#Subsequence
def subseq(s, i, curr, res):
    if i == len(s):
        if curr:  
            res.append(curr)
        return
    subseq(s, i + 1, curr + s[i], res)
    subseq(s, i + 1, curr, res)

def lexo(s):
    res = []
    subseq(s, 0, "", res)
    res.sort() 
    print(" ".join(res))  


s = input().strip()
lexo(s)

