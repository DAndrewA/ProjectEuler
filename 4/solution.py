def isPalindrome(string):
    if string[::-1] == string:
        return True
    else:
        return False

'''
number1 = 999
palindrome = 0
while number1 > 99:
    number2 = 999
    while number2 > 99:
        product = number1 * number2
        productString = str(product)
        if isPalindrome(productString):
            if product > palindrome:
                palindrome = product
                print("New largest palindrome: " + str(palindrome))
            print("SUCCESFUL PRODUCT: " + productString)
            print(number1,number2)
        number2 = number2 - 1
    number1 = number1 - 1

print(palindrome)
'''
highestPalindrome = 0
# change start value of x to limit number of calculations
for x in range(800,1000):
    for y in range(100,1000):
        xy = x*y
        if isPalindrome(str(xy)):
            if xy > highestPalindrome:
                highestPalindrome = xy
print(highestPalindrome)
