class Solution:
    def lengthOfLastWord(self, s: str) -> int:                
        end = len(s) - 1

        while s[end] == " ":
            end -= 1
        
        start = end
        while start >= 0 and s[start] != " ":
            start -= 1
        
        return end - start
        


        # initial plan
        # start from the end
        # count until you find an empty space
        # return the number.

        # final solution
        # s[end] == " ", to skip spaces at the end of the string
        # get the end and start
        # calculate difference between start and end