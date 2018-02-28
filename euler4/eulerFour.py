import math
#------------------------------------------------------
def digits(x):

    digits = int(math.log10(x))+1
    return digits

def reverse(y):
    number = int(y)
    reverse = 0

    while(number > 0):
        remainder = number % 10
        reverse = (reverse * 10) + remainder
        number = number // 10

    return int(reverse)

def palindromic():

    ans = max(i * j
        for i in range(100, 1000, 2)
        for j in range(100, 1000, 2))

    return int(ans)
#------------------------------------------------------
def main():

    print(palindromic())
    print('lmao')

if __name__ == "__main__":
    main()
