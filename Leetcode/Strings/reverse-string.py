class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]




        # arrays: stores numbers, strings or any collection of items
        # strings: stores words, letters ot sentences

        # initial plan
        # store the values in a stack and pop the values out

        # final solution
        # s[::-1] creates a reversed version of the list s
        # s[:] replace the contents of s with the contents on the right
        # slice notation
        # s[::-1] , s[start:stop:step], no start or stop, so go from beginning to end, -1 so move backwards through the list.


     

        