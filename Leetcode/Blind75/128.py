class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if n - 1 not in num_set:
                length = 1

                while n + length in num_set:
                    length += 1
                
                longest = max(longest, length)
        
        return longest
        
        # create a set from the input list
        # if the number right before n is not in the set, then n might be the first in a new sequence. 
        # then move on to the next sequence. 
        # choose the longest sequence available in the string. 
        # time complexity: O(N). The loop iterates over each element in num_set and expands forward with the while loop. 
        # each lookup and insertion in a set is O(1)
        # space complexity is O(N)
        # store all values from nums into a set which requires space. 