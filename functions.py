# Function to convert binary to decimal
def to_decimal(binary_num: str):

    num_qty = len(binary_num)-1
    decimal_num = 0

    for i in range(0, len(binary_num)):

        decimal_num += int(binary_num[i])*(2**num_qty)
        num_qty -= 1

    return str(decimal_num)

# Function to convert decimal to binary
def to_binary(decimal_num: str):

    decimal_num = int(decimal_num)
    binary_num = ''

    while decimal_num > 0:
        quotient = decimal_num // 2
        binary_num = str(decimal_num % 2) + binary_num
        decimal_num = quotient
    
    return binary_num
