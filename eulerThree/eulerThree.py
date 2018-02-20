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

def largestPrimeFactors(b):
    largest = []

    for i in range(1, int(b**0.5)+1):
        if b%i == 0:
            largest.append(b//i)

    for z in range(len(largest)):
        if isPrime(largest[z]) == False:
            largest.pop(z)

    print(largest)


def main():
    number = input('Enter number to test: ')
    #print (isPrime(number))
    largestPrimeFactors(number)

if __name__ == "__main__":
    main()
