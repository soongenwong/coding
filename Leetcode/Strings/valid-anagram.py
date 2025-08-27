class Solution:
    def isAnagram(self, s: str, t: str) -> bool:  
        if len(s) != len(t):
            return False

        counter = {}

        for char in s:
            counter[char] = counter.get(char, 0) + 1

        for char in t:
            if char not in counter or counter[char] == 0:
                return False
            counter[char] -= 1

        return True
        

        # initial plan 
        # store values of s, and seacrh t if all values are found. 

        # final solution 
        # counter.get(char, 0) + 1 returns teh current count of char in the dictionary counter, or 0 if char isn't there. add 1 to update the count. 
        # if char is not in counter is counter for the character is 0, return false. 
        # after the char is found in t, remove from counter[char]