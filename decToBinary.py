def decimalToBinary(userInput):
    i = 7 #used for the number of times to carry out the multiplication process in the while loop below (i.e. how many decimal places to go to)
    #I put i = 7 because if you enter a number like 0.14 and only have i = 4, then it won't be entirely accurate for this process
    decimalNumber = float(userInput) #converting userInput to a float
    signBit = str(1-(decimalNumber>=0)) #determines either 0 or 1 for signbit based on truth value for decimalNumber>=0
    wholePart = int(str(decimalNumber).split(".").pop(0)) #splits decimal in two parts into a list, then returns the whole number portion at index 0 with pop, converts that number to an int
    decimalNumber -= wholePart #gets the number after the decimal point, so if it was 12.5, it would give 0.5
    if(signBit == "0"):
        binaryForm = bin(wholePart).lstrip("0b") + "." #converting int to binary and strips the "0b" python gives
    else:
        binaryForm = bin(wholePart).lstrip("-0b") + "." #if number is negative, required to strip the negative sign as well
    # binaryForm = bin(wholePart).lstrip("0b") + "." if signBit =="0" else bin(wholePart).lstrip("-0b") + "." #condensed if/else if I wanted to condense it even more
    decimalNumber = abs(decimalNumber) #in case it is negative for the next steps
    while(i): #while i is not 0
        decimalNumber *= 2 #multiply decimal part by 2 
        if(decimalNumber >= 1.0): #if decimal part is 1 after multiplication, stop
            binaryForm += "1" #add a "1" to the binaryForm string
            decimalNumber -= 1 #subtract the number by 1 if it is greater than or equal to one
        else:
            binaryForm += "0" #add a "0" to the binaryForm string
        i -= 1 #decrements i by one accordingly until it hits zero according to the significand places
    print("Answer for question 1:", binaryForm) #answer for #1
    normalizedWithExponent = "{0:.4E}".format(float(binaryForm)) #normalizing with scientific notation
    print("Answer for question 2:", normalizedWithExponent) # in normalized scientific notation
    decimalPortion = normalizedWithExponent.split(".") #first splitting off the 1. of the number
    decimalPortion = decimalPortion[1].split("E") #then splitting off the significand and exponent into a list
    significand = decimalPortion[0]
    exponent = int(decimalPortion[1]) #converting the exponent into an integer for the step below
    exponentExcess = bin(exponent + 3).lstrip("0b") #adding 3 to the exponent, converting to binary, and then stripping the 0b the compiler adds
    eightBitCell(signBit, exponentExcess.zfill(3), significand) #zfill is required here due to the compiler not giving enough zeroes for the exponent
def eightBitCell(sign, exp, sig): #decided to split these print statements into its own function
    print("The sign bit is:", sign, "\nThe exponent is:", exp, "\nThe significand is:", sig)
    print("The final result is:", sign + exp + sig) #concatenating strings for a final result (8 bit cell)
if __name__ == "__main__": 
    print("Please enter a decimal number that you want to convert into a binary number in excess 3, 8 bit cell notation.\n")
    print("The decimal part will be rounded to 7 places for accuracy in the first step.\n") 
    decimalString = input("Your decimal number:") #getting user input as string
    decimalToBinary(decimalString)






