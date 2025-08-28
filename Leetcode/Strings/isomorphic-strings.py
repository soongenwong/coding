class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_index_s = {}
        char_index_t = {}

        for i in range(len(s)):
            if s[i] not in char_index_s:
                char_index_s[s[i]] = i

            if t[i] not in char_index_t:
                char_index_t[t[i]] = i
            
            if char_index_s[s[i]] != char_index_t[t[i]]:
                return False

        return True


        # initial plan
        # seach for the same values in s
        # look for the corresponding positions in t, if they are the same, true, else, false. 

        # final solution 
        # if the value in s is not in char_index_s, add it.
        # if the value in t is not in char_index_t, add it.
        # check if the way characters are mapped from s to t is consistent for all positions. 
        # char_index_s[s[i]] stores the first index where s[i] appears in s
        # if the mapping is correct, the char_index_s[s[i]] will be the same

        