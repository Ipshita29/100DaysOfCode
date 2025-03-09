#Generate Binary Strings
def generate_binary_strings(N):
    for num in range(2**N):  
        print(format(num, f'0{N}b'))  
N = int(input())
generate_binary_strings(N)