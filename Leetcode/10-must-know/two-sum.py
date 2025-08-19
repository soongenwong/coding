class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        n = len(nums)

        for i in range (n):
            complement = target - nums[i]
            if complement in numMap:
                return [numMap[complement], i]
            numMap[nums[i]] = i

        return []

        #initial plan
        # use hashmap to store the numbers
        # use queue to find the value for the sum. 
        # subtract from target to the value, and search for the other value. 



        # final solution
        # index: singular, indices: plural
        # use hash map(dictionary) to store element and their indices.
        # complement = target - nums[i]
        # check if the complement exists in the hash table. 
        # if complement does not exist, add nums[i] to hash table with the index
        # repeat until you find a solution or reach the end of the array.

        #initialise an empty dictionary to store numbers and indices
        # loop through every element
        # complement = target - nums[i]
        # if complement is in numMap, return the indices. else, add the number and index to numMap.
        # if no match , return empty list

        # summary: saves the number in a hash map, so don't have to loop twice. 