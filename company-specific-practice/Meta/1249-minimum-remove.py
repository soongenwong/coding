class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        
        while stack:
            s[stack.pop()] = ''
        
        return ''.join(s)

        # final solution
        # The code uses a stack to track unmatched opening parentheses.

        # It removes unmatched closing parentheses on the fly.

        # It removes any remaining unmatched opening parentheses at the end.

        # The result is a valid string with the minimum number of removals.
        