def replace_with_zero(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i > j:
                matrix[i][j] = 0
    return matrix


def main():
    rows = int(input("Enter the number of rows: "))
    matrix = []
    for i in range(rows):
        matrix.append([int(x) for x in input().split()])
    print(replace_with_zero(matrix))


if __name__ == '__main__':
    main()
