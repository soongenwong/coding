class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False

        return not stack
        


        # initial plan
        # use two pointers and hasp map.
        # note down the first opening bracket. 
        # search from the back and find the closing bracket. If it is found, match both together.
        # next, continue to the next opening bracket from the front. 
        # search from the back to find the corresponding closing bracket. repeat.
        # before closign the match from the closing bracket, make sure that there is no half set within. 
        


        # final solution
        # paranthesis: singular, parantheses: plural
        # use hashmap and stack
        # stack only has open parentheses. 
        # when there is a close paranthesis, use it as a key to find valid open parantheses in the mapping. 
        #if the two parantheses (the current close paranthesis and the latest paranthesis in stack) are not a valid combination, return false.
        # if stack is empty, return true.

        #summary: stack: check, hashmap: match.