class Solution:
    def setZeroes(self, matrix):
        m = len(matrix)
        n = len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Check first row
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True

        # Check first column
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True

        # Mark rows and columns
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero marked rows
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        # Zero marked columns
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # Zero first row
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Zero first column
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0