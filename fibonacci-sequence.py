fibonacciResult = []
currentNumber = 1
previousNumber = 0
fibonacciResult.append(currentNumber)

while len(fibonacciResult) < 10:
    result = currentNumber + previousNumber
    previousNumber = currentNumber
    currentNumber = result

    fibonacciResult.append(currentNumber)

print(fibonacciResult)
