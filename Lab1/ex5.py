def print_spiral(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1
    direction = 0
    # 0 - st dr, 1 - sus jos, 2 - dr st, 3 - jos sus
    while top <= bottom and left <= right:
        if direction == 0:
            for i in range(left, right + 1):
                print(matrix[top][i], end=" ")
            top += 1
        elif direction == 1:
            for i in range(top, bottom + 1):
                print(matrix[i][right], end=" ")
            right -= 1
        elif direction == 2:
            for i in range(right, left - 1, -1):
                print(matrix[bottom][i], end=" ")
            bottom -= 1
        elif direction == 3:
            for i in range(bottom, top - 1, -1):
                print(matrix[i][left], end=" ")
            left += 1
        direction = (direction + 1) % 4


def main():
    matrix = [[1, 2, 3, 4],
              [12, 13, 14, 5],
              [11, 16, 15, 6],
              [10, 9, 8, 7]]
    print_spiral(matrix)


main()
