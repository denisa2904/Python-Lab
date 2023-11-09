def is_palindrome(num):
    return num == num[::-1]


def main():
    num = input("Enter a number: ")
    print(is_palindrome(num))


if __name__ == '__main__':
    main()
