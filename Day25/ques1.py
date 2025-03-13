#Count Even factors
def countEvenFactors(n):
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0: 
            if i % 2 == 0:
                count += 1 
            if (n // i) % 2 == 0 and i != (n // i):
                count += 1 
    return count
n = int(input())
print(countEvenFactors(n))