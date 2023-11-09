def not_null_bits(num):
    cnt = 0
    while num > 0:
        if num % 2 == 1:
            cnt += 1
        num //= 2
    return cnt


def main():
    num = int(input("Enter a number: "))
    print(not_null_bits(num))


if __name__ == '__main__':
    main()
