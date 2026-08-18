class Solution:
    def largestInteger(self, nums, k):
        n = len(nums)
        result = -1
        
        for x in set(nums):
            count = 0
            for start in range(n - k + 1):
                window = nums[start:start + k]
                if x in window:
                    count += 1
                    if count > 1:
                        break
            if count == 1:
                result = max(result, x)
        
        return result