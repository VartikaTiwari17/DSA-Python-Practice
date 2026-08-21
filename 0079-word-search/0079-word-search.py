class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])

        def dfs(r, c, index):
            # Word completely found
            if index == len(word):
                return True

            # Out of bounds
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            # Wrong character
            if board[r][c] != word[index]:
                return False

            # Mark current cell as visited
            temp = board[r][c]
            board[r][c] = '#'

            # Check 4 directions
            found = (
                dfs(r + 1, c, index + 1) or
                dfs(r - 1, c, index + 1) or
                dfs(r, c + 1, index + 1) or
                dfs(r, c - 1, index + 1)
            )

            # Restore cell
            board[r][c] = temp

            return found

        # Try every cell as starting point
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False