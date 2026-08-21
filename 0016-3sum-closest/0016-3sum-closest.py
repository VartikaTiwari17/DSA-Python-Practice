class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                # Exact answer mil gaya
                if total == target:
                    return total

                # Closest answer update karo
                if abs(total - target) < abs(closest - target):
                    closest = total

                # Target ke according pointers move karo
                if total < target:
                    left += 1
                else:
                    right -= 1

        return closest