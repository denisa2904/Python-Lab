def get_set(list1):
    return [len(set(list1)), len(list1) - len(set(list1))]


def main():
    list1 = [1, 1, 2, 2, 4, 5, 6, 7, 8, 9]
    print(get_set(list1))


if __name__ == '__main__':
    main()