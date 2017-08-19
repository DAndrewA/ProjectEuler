# using the mathematical series formula for n and n^2
nMax = 100
sigSquares = nMax*(nMax+1)*((nMax*2)+1)//6
squareSum = (nMax*(nMax+1)//2)**2
value = squareSum-sigSquares
print(value)
