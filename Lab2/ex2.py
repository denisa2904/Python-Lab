def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def main():
    num = input("Enter a list of numbers: ").split()
    for i in range(len(num)):
        if is_prime(int(num[i])):
            print(num[i], end=" ")


if __name__ == '__main__':
    main()
