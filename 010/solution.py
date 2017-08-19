cap = 2000000
primes = [p for p in range(2,cap) if 0 not in [p % n for n in range(2,int(p**0.5)+1)]]
t = 0
for p in primes:
    t += p
print(t)
