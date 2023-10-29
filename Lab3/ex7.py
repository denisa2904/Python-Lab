def get_sets(*args):
    result = {}
    for i in range(len(args)):
        for j in range(i + 1, len(args)):
            result[str(args[i]) + ' | ' + str(args[j])] = args[i] | args[j]
            result[str(args[i]) + ' & ' + str(args[j])] = args[i] & args[j]
            result[str(args[i]) + ' - ' + str(args[j])] = args[i] - args[j]
            result[str(args[j]) + ' - ' + str(args[i])] = args[j] - args[i]
    return result


def main():
    a = {1, 2, 3}
    b = {3, 4, 5}
    print(get_sets(a, b))


if __name__ == '__main__':
    main()