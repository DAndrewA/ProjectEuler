numberFound = False
# last number known to be not divisible
number = 45000
print("RUNNING")
while numberFound == False:
    remainder = 0
    for i in range(1,21):
        remainder += number % i
    if remainder == 0:
        print(number)
        numberFound = True
    number += 1
