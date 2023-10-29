def ascii_code(x=1, strings=None, flag=True):
    if strings is None:
        strings = []
    result = []
    if flag:
        for i in range(len(strings)):
            result.append([])
            for j in range(len(strings[i])):
                if ord(strings[i][j]) % x == 0:
                    result[i].append(strings[i][j])
    else:
        for i in range(len(strings)):
            result.append([])
            for j in range(len(strings[i])):
                if ord(strings[i][j]) % x != 0:
                    result[i].append(strings[i][j])
    return result


def main():
    strings = input("Enter a list of strings: ").split()
    print(ascii_code(2, strings, False))
    print(ascii_code(2, strings))


if __name__ == '__main__':
    main()
