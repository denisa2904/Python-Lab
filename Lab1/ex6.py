def is_palindrome(num):
    reverse_num = num[::-1]
    if num == reverse_num:
        return True
    return False


# def main():
#     num = input("Enter a number: ")
#     print(is_palindrome(num))
#
#
# if __name__ == '__main__':
#     main()
