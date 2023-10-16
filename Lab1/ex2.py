def count_vowels(string):
    count = 0
    for i in string:
        if i in 'aeiou':
            count += 1
    return count


def main():
    word = input("Enter a string: ")
    print(count_vowels(word))

if __name__ == '__main__':
    main()
