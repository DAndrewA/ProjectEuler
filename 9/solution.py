# plan is to go through complex plain at grid points, then square the numbers to receive integr bsolutions to pythagorian triplets
# a^2 + b^2 = c^2 such that a < b < c
found = False
x,y = 2,1
while not found:
    # getting the values for a, b and c
    a = (x**2) - (y**2)
    b = 2*x*y
    c = x**2 + y**2
    # printing the triplets
    print(a,b,c)

    if a+b+c == 1000:
        found = True
        print("Solution found:")
        print("abc = ",a*b*c)

    if x-1 > y:
        y += 1
    else:
        x += 1
        y = 1
