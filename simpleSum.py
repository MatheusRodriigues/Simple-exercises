listOfPieces = []
i = 2

while i != 0:
    partInfo = []

    quantityOfPieces = int(input("Enter the quantity of pieces: "))
    partCode = int(input("Enter the party code: "))
    valueOfParts = float(input("Enter the value of the part: "))

    partInfo.append(partCode)
    partInfo.append(quantityOfPieces)
    partInfo.append(valueOfParts)

    listOfPieces.append(partInfo)

    i -= 1

amount = (listOfPieces[0][2] * listOfPieces[0][0]) + (listOfPieces[1][2] * listOfPieces[1][0])

print("Amount to pay: $ {:.2f}".format(amount))