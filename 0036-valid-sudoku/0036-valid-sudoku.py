class Solution:
    def isValidSudoku(self, board):

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):

                value = board[r][c]

                if value == ".":
                    continue

                # 3x3 box ka number
                box = (r // 3) * 3 + (c // 3)

                # Duplicate check
                if value in rows[r]:
                    return False

                if value in cols[c]:
                    return False

                if value in boxes[box]:
                    return False

                # Value add karo
                rows[r].add(value)
                cols[c].add(value)
                boxes[box].add(value)

        return True