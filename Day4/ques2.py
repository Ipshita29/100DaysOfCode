#Prefix Removals
#You are given a string s consisting of lowercase letters of the English alphabet. You must perform the following algorithm on s Let x be the length of the longest prefix of s which occurs somewhere else in s as a contiguous substring (the other occurrence may also intersect the prefix). If x=0, break. Otherwise, remove the first x characters of s, and repeat.
t = int(input()) 
for _ in range(t):
    s = input().strip()
    seen = set()
    for i in range(len(s)):
        seen.add(s[i])
        if s[i] in s[i + 1:]:  
            continue
        print(s[i:])  
        break