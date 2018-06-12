def isPrime(n):
    if n==2 or n==3:
         return True
    elif n%2==0 or n<2:
         return False

    for i in range(3,int(n**0.5)+1,2):   # only odd numbers
        if n%i==0:
            return False

    else:
         return True

def primeFinder():

    primeList = [2, 3, 5, 7, 11, 13]
    i = 1

    while len(primeList) < 10001:
        if isPrime(primeList[-1] + i):
            primeList.append(primeList[-1] + i)
            i = 1
        else:
            i += 1

    return iter(primeList)

def main():

    print("The 10,001th prime number is %d" % max(primeFinder()))

if __name__ == "__main__":
    main()
