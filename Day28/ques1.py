#Find the K-th Character in String Game I
def kthCharacter(k):
    def find_kth(k, n):
        if n == 0: 
            return "a"

        length_n_minus_1 = 2 ** (n - 1)  

        if k <= length_n_minus_1:
            return find_kth(k, n - 1)  
        else:
            prev_char = find_kth(k - length_n_minus_1, n - 1) 
            return chr(ord(prev_char) + 1) if prev_char != 'z' else 'a'  

    n = 0
    while (1 << n) < k:  
        n += 1

    return find_kth(k, n)

