# I misunderstood meaning of square-free, and 4k+1 < 150, not N.
# Possible for N to be all the primes multiplied together



# generates all primes below the cap that are of the form 4k+1
def gen4kPrimes(cap):
    primes = [x for x in range(3,cap,2) if 0 not in [x % a for a in range(2,int(x**0.5)+1)] and x % 4 == 1])
    print("Primes: ",primes)
    return primes

'''
# get all integers below the cap that are divisible by primes of the form 4k+1 and aren't square
def getIntegers(cap,primeArray):
    integers = []
    for p in primeArray:
        for i in range(1,(cap//p) + 1):
            if p*i not in integers and i != p and p*i < cap:
                integers.append(p*i)
    print("Integers: ",integers)
    return integers
'''

def getIntegers(cap,primeArray):
    integers = []
    for p in primeArray:
        for p2 in primeArray:
            if p*p2 not in integers and p2 != p and p*p2 < cap:
                integers.append(p*p2)
    print("Integers: ",integers)
    return integers

# gets all combinations of pairs of integer squares below the cap
def getSquaresCombos(cap):
    squaresCombos = []
    for i in range(1,int((cap**0.5))):
        s = i
        while (i**2) + (s**2) < cap:
            sumP = (i**2) + (s**2)
            if [i,s,sumP] not in squaresCombos:
                squaresCombos.append([i,s,sumP])
            s += 1
    print("Square combinations: ",squaresCombos)
    return squaresCombos

# gets the sum of all a where a^2 + b^2 = N, where N < cap and N is divisible by primes of the form 4k+1
def getSumOfA(squareCombos,integers):
    total = 0
    for combo in squareCombos:
        if combo[2] in integers:
            print(combo)
            total += combo[0]
    print("Total: ",total)
    return total


cap = 150
primes = gen4kPrimes(cap)
integers = getIntegers(cap,primes)
squareCombos = getSquaresCombos(cap)
total = getSumOfA(squareCombos,integers)
