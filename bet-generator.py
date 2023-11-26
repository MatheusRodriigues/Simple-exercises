import random

quantityOfNumbers = int(input("Enter the quantity of numbers to be generate: "))
smallestNumber = int(input("Smallest number to be generate: "))
largestNumber = int(input("Largest number to be generate: "))

listOfNumbers = []

while quantityOfNumbers > 0:
    rNumber = random.randrange(smallestNumber, largestNumber)
    if rNumber in listOfNumbers:
        pass
    else:
        listOfNumbers.append(rNumber)
    
    quantityOfNumbers -= 1

print(listOfNumbers)