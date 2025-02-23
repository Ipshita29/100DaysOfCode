#Given a string s of zeros and ones, return the maximum score after splitting the string into two non- empty substrings (i. e. left substring and right substring). The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.
def maxScore(s):
    total_one = s.count('1')  
    left_zero = 0  
    right_one = total_one  
    max_score = 0 
    for i in range(len(s) - 1):
        if s[i] == '0':
            left_zero += 1  
        else:
            right_one -= 1  
        max_score = max(max_score, left_zero + right_one)
    return max_score

    