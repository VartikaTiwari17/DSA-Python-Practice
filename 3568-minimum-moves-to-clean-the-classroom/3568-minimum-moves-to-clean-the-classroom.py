from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m, n = len(classroom), len(classroom[0])

        start = None
        litters = []

        # Find starting position and all litter cells
        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litters.append((r, c))

        k = len(litters)

        if k == 0:
            return 0

        # Assign each litter a bit index
        litter_index = [[-1] * n for _ in range(m)]

        for i, (r, c) in enumerate(litters):
            litter_index[r][c] = i

        full_mask = (1 << k) - 1

        # visited[r][c][mask] = maximum energy remaining
        visited = [[[-1] * (1 << k) for _ in range(n)] for _ in range(m)]

        sr, sc = start

        # (row, col, collected_mask, remaining_energy, moves)
        queue = deque([(sr, sc, 0, energy, 0)])
        visited[sr][sc][0] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            r, c, mask, remaining, moves = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                # Check boundaries
                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                # Cannot pass obstacle
                if classroom[nr][nc] == 'X':
                    continue

                # Need energy to move
                if remaining == 0:
                    continue

                new_energy = remaining - 1
                new_mask = mask

                # Collect litter
                if litter_index[nr][nc] != -1:
                    new_mask |= (1 << litter_index[nr][nc])

                # Reset energy
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                # All litter collected
                if new_mask == full_mask:
                    return moves + 1

                # Skip if already visited with equal or more energy
                if visited[nr][nc][new_mask] >= new_energy:
                    continue

                visited[nr][nc][new_mask] = new_energy
                queue.append(
                    (nr, nc, new_mask, new_energy, moves + 1)
                )

        return -1