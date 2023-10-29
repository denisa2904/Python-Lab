def get_sets(a, b):
    return [set(a) & set(b), set(a) | set(b), set(a) - set(b), set(b) - set(a)]


def main():
    a = [1, 2, 3, 4, 5]
    b = [3, 4, 5, 6, 7]
    print(get_sets(a, b))


if __name__ == '__main__':
    main()