numPrime = 10001
numFound = 1
prime = 2
currentNum = 1

def isPrime(n):
    if 0 not in [n % a for a in range(2,int(n**0.5)+1)]:
        return True
    else:
        return False

while numFound < numPrime:
    currentNum += 2
    if isPrime(currentNum):
        numFound += 1
        prime = currentNum
print(prime)
