class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, remaining, path):
            if remaining == 0:
                result.append(path[:])
                return

            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                num = candidates[i]

                if num > remaining:
                    continue

                path.append(num)

                # i hi pass kar rahe hain
                # kyunki same number dobara use kar sakte hain
                backtrack(i, remaining - num, path)

                path.pop()

        candidates.sort()
        backtrack(0, target, [])

        return result