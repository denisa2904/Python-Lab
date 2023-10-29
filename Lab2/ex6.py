def appear_x_times(x, *lists):
    result = []
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            count = 0
            for k in range(len(lists)):
                for m in range(len(lists[k])):
                    if lists[i][j] == lists[k][m]:
                        count += 1
            if count == x and lists[i][j] not in result:
                result.append(lists[i][j])
    return result


def main():
    print(appear_x_times(3, [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7]))
    print(appear_x_times(2, [1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [3, 4, 5, 6, 7], [1, 2, 3, 4, 5]))


if __name__ == '__main__':
    main()
