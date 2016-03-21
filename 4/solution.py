def isPalindrome(string):
    if string[::-1] == string:
        return True
    else:
        return False

number1 = 999
palindromeFound = False
while palindromeFound == False:
    number2 = 999
    while palindromeFound == False and number2 > 0:
        product = number1 * number2
        productString = str(product)
        if isPalindrome(productString):
            palindromeFound = True
            print(product)
        number2 = number2 - 1
    number1 = number1 - 1
