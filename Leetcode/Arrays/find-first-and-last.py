class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(nums, target, is_searching_left):
            left = 0
            right = len(nums) - 1
            idx = -1
            
            while left <= right:
                mid = (left + right) // 2
                
                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    idx = mid
                    if is_searching_left:
                        right = mid - 1
                    else:
                        left = mid + 1
            
            return idx
        
        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)
        
        return [left, right]
            
                



        # initial plan
        # use binary search
        # split into half and search.

        # final solution
        # idx = store the most recent index where the target element is found. 
        # is_searching_left is to find the range of the target. 
        # final part where left = binary_search is to find the leftmost index of the target. 