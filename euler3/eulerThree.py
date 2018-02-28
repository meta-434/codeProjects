#determines if a given number is isPrime
#a - number to check prime.
def gpfFinder(a):
    a = abs(int(a))
    gpf = 2

    if a < 2: # 1 and 0 are not prime
        print("1 and 0 do not have prime factors.")
        raise SystemExit
    elif a == 2: # 2 is smallest prime and only even prime
        return a
    else:
        while a > gpf:
            if a%gpf == 0:
                a = a/gpf
            else:
                gpf += 1
        return gpf

#------------------------------------------------------
def main():
    usrIn = int(input("enter number: "))
    print("greatest prime factor of %d is %d" %(usrIn, gpfFinder(usrIn)))

if __name__ == "__main__":
    main()
