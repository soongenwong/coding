class Solution:
    def maxArea(self, height: List[int]) -> int:
      left = 0
      right = len(height) - 1
      maxArea = 0

      while left < right:
        currentArea = min(height[left], height[right]) * (right - left)
        maxArea = max(currentArea, maxArea)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
      return maxArea