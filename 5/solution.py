highestInteger = 20

def getPrimeFactors(n):
    primeFactors = {}
    while n > 1:
        p = True
        i = 1
        while p:
            i += 1
            if n % i == 0:
                p = False
                if i in primeFactors:
                    primeFactors[i] += 1
                else:
                    primeFactors[i] = 1
                n = n//i
                break
            if n == int(n**0.5):
                p = False
        if p:
            primeFactors[n] = 1
            n = 1
    print(primeFactors)
    return primeFactors

primeFactorsArr = []
productFactors = {}
# getting prime factors of n from 1 to 20
for i in range(1,highestInteger+1):
    primeFactorsArr.append(getPrimeFactors(i))
# getting the highest power of each prime factor accross all the sets
for factorSet in primeFactorsArr:
    for factor in factorSet:
        if factor not in productFactors:
            productFactors[factor] = factorSet[factor]
        else:
            if factorSet[factor] > productFactors[factor]:
                productFactors[factor] = factorSet[factor]
# creating the product
print("productFactors : " , productFactors)
product = 1
for factor in productFactors:
    product = product * (factor**productFactors[factor])
print(product)
