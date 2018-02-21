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

#returns the factors of a given number.
#if given number is prime, returns 0
#b - number to factor.
def factors(b):
    listFactors = []

    for i in range(2, int(b**0.5)+1):
        if b%i == 0:
            listFactors.append(int(b/i))
            #listFactors.append(int(i)) #for more context de-comment

    return listFactors
    
#main function. calls isPrime on factors list result to filter
#and max() to determine greatest prime factor from user input.
def main():
    number = int(input('Enter number to test: '))
    listNumber = factors(number)

    if len(listNumber) == 0:
        print("input is prime. largest prime factor is %d." % number)
    else:
        for z in range(0, len(listNumber)):
            if isPrime(listNumber[z]) == False:
                listNumber.pop([z])

        print("largest prime factor is %d" % int(max(listNumber)))

# main execution conditional
if __name__ == "__main__":
    main()
