class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]

        for i in range(min(len(first), len(last))):
            if(first[i] != last[i]):
                return ans
            ans += first[i]
        
        return ans




        # initial plan
        # use hashmap
        # sort alphabetically, compare first and last value. take the common term. 


        #final solution
        # sort the string.
        # loop through the characters of the first and last, up to the length of the shorter string. 
        # if characters are different, return the answer
        # if characters are the same, add value to answer

        # summary: compare first and last, if same, add to answer, if different, return answer.