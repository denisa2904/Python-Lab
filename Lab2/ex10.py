def tuple_lists(*lists):
    result = []
    for i in range(max([len(x) for x in lists])):
        result.append([])
        for j in range(len(lists)):
            if i < len(lists[j]):
                result[i].append(lists[j][i])
            else:
                result[i].append(None)
    return result


def main():
    print(tuple_lists([1, 2, 3, 4], [5, 6, 7], ["a", "b", "c"]))


if __name__ == '__main__':
    main()