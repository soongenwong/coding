class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
        


        # initial plan
        # find when the values stop increasing in ascending order. 
        # shift it back to ascending order when the value is found. 
        # do the usual to find the target

        # final solution 
        # do the usual searching of values
        # if nums[mid] >= nums[left] means that left half is sorted. 
        # if target is in left half, if target is in right half.