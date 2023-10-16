def count_words(phrase):
    cnt = 0
    for i in phrase:
        if i == ' ':
            cnt += 1

    return cnt + 1


def main():
    phrase = input("Enter a phrase: ")
    print(count_words(phrase))


if __name__ == '__main__':
    main()
