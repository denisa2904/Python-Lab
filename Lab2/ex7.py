def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    return False


def palindrome(numbers):
    count = 0
    max_val = 0
    for i in range(len(numbers)):
        if is_palindrome(numbers[i]):
            count += 1
            if numbers[i] > max_val:
                max_val = numbers[i]
    return count, max_val


def main():
    numbers = [int(x) for x in input("Enter a list of numbers: ").split()]
    print(palindrome(numbers))


if __name__ == '__main__':
    main()

