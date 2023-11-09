def fibo(n):
    list1 = []
    a, b = 0, 1
    while a < n:
        list1.append(a)
        c = a
        a = b
        b = c + b
    return list1


def main():
    n = int(input("Enter a number: "))
    print(fibo(n))


if __name__ == '__main__':
    main()

