class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.matrix = [[0 for x in range(m)] for y in range(n)]

    def __getitem__(self, index):
        if isinstance(index, tuple) and len(index) == 2:
            row, col = index
            if 0 <= row < self.n and 0 <= col < self.m:
                return self.matrix[row][col]
            else:
                raise IndexError("Index out of range")
        else:
            raise TypeError("Index must be a tuple of two integers")

    def __setitem__(self, index, value):
        if isinstance(index, tuple) and len(index) == 2:
            row, col = index
            if 0 <= row < self.n and 0 <= col < self.m:
                self.matrix[row][col] = value
            else:
                raise IndexError("Index out of range")
        else:
            raise TypeError("Index must be a tuple of two integers")

    def transpose(self):
        return [[self.matrix[x][y] for x in range(self.n)] for y in range(self.m)]

    def __mul__(self, matrix):
        if self.m != matrix.n:
            return None
        result = [[0 for x in range(matrix.m)] for y in range(self.n)]
        for i in range(self.n):
            for j in range(matrix.m):
                for k in range(self.m):
                    result[i][j] += self.matrix[i][k] * matrix.matrix[k][j]
        return result

    def __str__(self):
        return str(self.matrix)
