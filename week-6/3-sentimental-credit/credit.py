import math

def main():
    while True:
        try:
            creditCard = int(input("What's your credit card?: "))
            break
        except ValueError:
            print("Input only numbers!")
            print()

    sumOfEveryOtherDigit = everyOtherDigit(creditCard)
    cardDigits = len(str(creditCard))
    validAmex = isAmex(creditCard, cardDigits)
    validMaster = isMaster(creditCard, cardDigits)
    validVisa = isVisa(creditCard, cardDigits)

    if sumOfEveryOtherDigit % 10 != 0:
        print("INVALID")
    elif validAmex == True:
        print("AMEX")
    elif validMaster == True:
        print("MASTERCARD")
    elif validVisa == True:
        print("VISA")
    else:
        print("INVALID")

def everyOtherDigit(creditCard):
    counterSum = 0
    isAlternateDigit = False

    while creditCard > 0:
        if isAlternateDigit == True:
            lastDigit = creditCard % 10
            product = multiplySum(lastDigit)
            counterSum += product
        else:
            lastDigit = creditCard % 10
            counterSum += lastDigit
        isAlternateDigit = not isAlternateDigit
        creditCard = math.floor(creditCard / 10)
    return counterSum


def multiplySum(lastDigit):
    counterSum = 0
    multiply = lastDigit * 2
    while multiply > 0:
        lastDigitMultiplied = multiply % 10
        counterSum += lastDigitMultiplied
        multiply = math.floor(multiply / 10)
    return counterSum

def isAmex(creditCard, cardDigits):
    americEx = math.floor(creditCard / pow(10, 13))
    if cardDigits == 15 and (americEx == 34 or americEx == 37):
        return True
    else:
        return False

def isMaster(creditCard, cardDigits):
    masterCard = math.floor(creditCard / pow(10, 14))
    if cardDigits == 16 and (masterCard >= 51 and masterCard <= 55):
        return True
    else:
        return False

def isVisa(creditCard, cardDigits):
    if cardDigits == 13 or cardDigits == 16:
        power = cardDigits - 1
        visa = math.floor(creditCard / pow(10, power))
        if visa == 4:
            return True
        else:
            return False

if __name__ == "__main__":
    main()
