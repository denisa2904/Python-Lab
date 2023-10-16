def extract_number(phrase):
    number = 0
    is_number = 0
    for character in phrase:
        if character.isdigit():
            number = number * 10 + int(character)
            is_number = 1
        elif is_number == 1:
            break
    return number


# def main():
#     phrase = input("Enter a phrase: ")
#     print(extract_number(phrase))
#
#
# if __name__ == '__main__':
#     main()
