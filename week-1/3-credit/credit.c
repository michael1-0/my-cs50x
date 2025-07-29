#include <cs50.h>
#include <stdio.h>
#include <math.h>

int everyOtherDigit(long creditCard);
int multiplySum(int lastDigit);
int numOfDigits(long creditCard);
bool validAmex(long creditCard, int numDigits);
bool validMaster(long creditCard, int numDigits);
bool visacheck(long creditCard, int numDigits);

int main(void)
{
    long creditCard = get_long("Credit card: ");
    int sumEveryOtherDigit = everyOtherDigit(creditCard);
    int numDigits = numOfDigits(creditCard);
    bool amex = validAmex(creditCard, numDigits);
    bool master = validMaster(creditCard, numDigits);
    bool visa = visacheck(creditCard, numDigits);
    if (sumEveryOtherDigit % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }
    else if (amex == true)
    {
        printf("AMEX\n");
    }
    else if (master == true)
    {
        printf("MASTERCARD\n");
    }
    else if (visa == true)
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
        return 0;
    }
}

bool validAmex(long creditCard, int numDigits)
{
    int firstTwoDigits = creditCard / pow(10,13);
    if ((numDigits == 15) && (firstTwoDigits == 34 || firstTwoDigits == 37))
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool validMaster(long creditCard, int numDigits)
{
    int firstTwoDigits = creditCard / pow(10, 14);
    if ((numDigits == 16) && (firstTwoDigits > 50 && firstTwoDigits < 56))
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool visacheck(long creditCard, int numDigits)
{
     if (numDigits == 13 || numDigits == 16)
     {
          int i = numDigits - 1;
          int firstnum = creditCard / pow(10, i);

          if (firstnum == 4)
          {
               return true;
          }
          else
          {
               return false;
          }
     }
     return false;
}

int numOfDigits(long creditCard)
{
    int count = 0;
    while(creditCard > 0)
    {
        count = count + 1;
        creditCard = creditCard / 10;
    }
    return count;
}

int everyOtherDigit(long creditCard)
{
    int sum = 0;
    bool isAlternateDigit = false;
    while (creditCard > 0)
    {
        if (isAlternateDigit == true)
        {
            int lastDigit = creditCard % 10;
            int prod = multiplySum(lastDigit);
            sum = sum + prod;
        }
        else
        {
            int lastDigit = creditCard % 10;
            sum = sum + lastDigit;
        }
        isAlternateDigit = !isAlternateDigit;
        creditCard = creditCard / 10;
    }
    return sum;
}

int multiplySum(int lastDigit)
{
    int multiply = lastDigit * 2;
    int sum = 0;
    while (multiply > 0)
    {
        int lastDigitMultiplied = multiply % 10;
        sum = sum +  lastDigitMultiplied;
        multiply = multiply / 10;
    }
    return sum;
}
