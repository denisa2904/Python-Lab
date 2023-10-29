def spectators(matrix):
    shorties = []
    for j in range(len(matrix[0])):
        for i in range(1, len(matrix)):
            for k in range(0, i):
                if matrix[i][j] <= matrix[k][j]:
                    shorties.append([i, j])
                    break
    return shorties


def main():
    matrix = [[1, 2, 3, 2, 1, 1],
              [2, 4, 4, 3, 7, 2],
              [5, 5, 2, 5, 6, 4],
              [6, 6, 7, 6, 7, 5]]
    print(spectators(matrix))


if __name__ == '__main__':
    main()
