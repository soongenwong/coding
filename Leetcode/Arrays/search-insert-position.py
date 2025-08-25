class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
        
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else: 
                left = mid + 1
        
        return left





        # initial plan
        # use binary search to find the target value.
        # if the target value is not found, find the closest values and insert the target value. 

        # final solution
        # correct solution!
        # initialise the left and right positions. 
        # find the mid point. 
        # if mid = target, return mid
        # if mid > target, right = mid - 1
        # if mid < target, left = mid + 1
        # left and right are the indices. 
        # return left because that is the position to insert the target value.