def main():
    #sum of all natural numbers between 0 and 1000,
    #exclusive, that are multiples of 3 and 5
    x = 0
    y = 0

    while x < 1000:
        if x % 3 == 0 or x % 5 == 0:
            y += x
            x += 1
        else:
            x += 1

    return(y)

if __name__ == "__main__":
    print(main())
