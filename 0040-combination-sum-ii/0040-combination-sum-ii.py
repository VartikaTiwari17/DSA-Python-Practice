class Solution:
    def combinationSum2(self, candidates, target):
        result = []

        candidates.sort()

        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(candidates)):

                if candidates[i] > remaining:
                    break

                # Same level par duplicate skip karo
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])

                # i + 1 because each number can be used only once
                backtrack(i + 1, remaining - candidates[i], path)

                path.pop()

        backtrack(0, target, [])

        return result