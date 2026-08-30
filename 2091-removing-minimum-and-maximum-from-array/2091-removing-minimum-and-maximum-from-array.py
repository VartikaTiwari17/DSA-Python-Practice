class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        # Find indices of minimum and maximum
        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        left = min(min_index, max_index)
        right = max(min_index, max_index)

        # 1. Remove both from front
        from_front = right + 1

        # 2. Remove both from back
        from_back = n - left

        # 3. Remove one from front and one from back
        from_both = (left + 1) + (n - right)

        return min(from_front, from_back, from_both)