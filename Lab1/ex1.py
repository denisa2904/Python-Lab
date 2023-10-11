def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


def find_gcd(num):
    num1 = num[0]
    num2 = num[1]
    gcd_num = gcd(num1, num2)
    for i in range(2, len(num)):
        gcd_num = gcd(gcd_num, num[i])
    return gcd_num


def main():
    arr = [int(x) for x in input("Enter the numbers: ").split()]
    print(find_gcd(arr))


main()
