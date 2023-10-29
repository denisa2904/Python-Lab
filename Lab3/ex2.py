def count_char(text):
    dictionary = {}
    for char in text:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    return dictionary


def main():
    print(count_char('Ana has apples.'))


if __name__ == '__main__':
    main()
