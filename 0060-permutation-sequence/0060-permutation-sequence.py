class Solution:
    def getPermutation(self, n, k):
        nums = [str(i) for i in range(1, n + 1)]

        fact = 1
        for i in range(1, n):
            fact *= i

        k -= 1
        ans = ""

        while nums:
            index = k // fact
            ans += nums.pop(index)

            if not nums:
                break

            k %= fact
            fact //= len(nums)

        return ans