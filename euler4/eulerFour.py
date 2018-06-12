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

#NOT THE MOST OPTIMIZED WAY OF DOING THIS!!
def palindromic():

    ans = max(i * j
        for i in range(100, 1000)
        for j in range(100, 1000)
        if str(i * j) == str(i * j)[ : : -1])

    return str(ans)

#------------------------------------------------------
def main():

    print(palindromic())

if __name__ == "__main__":
    main()
