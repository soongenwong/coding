class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        return - 1
        


        # initial plan, use binary search by splliting the values into half. 
        # if value is found, return the index
        # if value is not found, return - 1
        # first question solved from scratch