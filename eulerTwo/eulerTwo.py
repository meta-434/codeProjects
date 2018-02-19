def main():

    index = 1
    total = 0
    fibb = [1, 1]

    while int(fibb[index]) < 4000000:
        fibb.append(int(fibb[index]) + int(fibb[index-1]))

        index += 1

    for x in fibb:
        if x%2 == 0:
            total += x
    print(total)

if __name__ == "__main__":
    main()
