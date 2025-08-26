class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_length = 0
        char_set = set()
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length



        # initial plan
        # search if the values are different
        # if they are different, add to the output
        # if the values are the same, move to the next value. 
        # return the number with the highest different values. 

        # final solution
        # use sliding window and set
        # left is the pointer, max_length is the value to return
        # char_set holds the unique characters currently in the window. 
        # char set is empty at the beginning
        # while s[right] in char set, there is a duplicate in the window, so remove s[left] 
        # add s[right] to char set
        # update max length
        