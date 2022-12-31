# Function to convert binary to decimal
def toDecimal(binaryNum=str):

    try:
        qtdNum = len(binaryNum)-1
        decimal = 0

        for i in range(0, len(binaryNum)):

            decimal += int(binaryNum[i])*(2**qtdNum)
            qtdNum -= 1

        return str(decimal)
        
    except:
        pass

# Function to convert decimal to binary
def toBinary(decimalNum=str):

    try:
        return str(bin(int(decimalNum))[2::])

    except:
        pass