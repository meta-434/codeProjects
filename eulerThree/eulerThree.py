#determines if a given number is isPrime
#a - number to check prime.
def isPrime(a):
    a = abs(int(a))

    if a < 2:
        return False
    if a == 2:
        return True
    if a>2 and a%2 == 0:
        return False
    for x in range(3, int(a**0.5) + 2, 2):
        if a % x == 0:
            return False
        return True
#returns the largest factor of a given number.
#if given number is prime, returns 0
#b - number to get largest factor.
def largestFactors(b):
    factors = []

    for i in range(2, int(b**0.5)+1):
        if b%i == 0:
            factors.append(int(b/i))

    if len(factors) == 0:
        print("number is prime... factors are 1 and itself.")
        return 0
    else:
        for j in range(0, len(factors)):
            if len(factors) == 1:
                #print(max(factors))
                return int(factors[j])
            else:
                #print(max(factors))
                return max(factors)

def main():
    number = input('Enter number to test: ')
    #print (isPrime(number))
    largestFactors(number)

if __name__ == "__main__":
    main()
