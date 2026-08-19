class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            width = right - left
            current_area = min(height[left], height[right]) * width
            max_area = max(max_area, current_area)
            
            # move the pointer at the shorter line, since it's the limiting factor
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area