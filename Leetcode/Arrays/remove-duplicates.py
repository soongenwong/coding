class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1

        for j in range(1, len(nums)):
            if nums[j] != nums[i - 1]:
                nums[i] = nums[j]
                i += 1

        return i        




        # initial solution
        # to understand, read the example. 
        # find the first number , add 1 to k, then find the second number then add to k

        # final solution
        # initialise i as index 1
        # if index 1 and index 0 are different, add index 1 to nums
        # add total value by 1 to i. 
