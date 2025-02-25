#Find The Diagonal Sum of a matrix
def calculate_diagonal_sum(matrix):
    N = len(matrix)  
    diag_sum = 0
    for i in range(N):
        diag_sum += matrix[i][i]  
        diag_sum += matrix[i][N - 1 - i]  
    if N % 2 == 1:
        diag_sum -= matrix[N // 2][N // 2] 
    return diag_sum

