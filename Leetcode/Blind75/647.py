class Solution:
    def countSubstrings(self, s: str) -> int:
	    L, r = len(s), 0
	    for i in range(L):
	    	for a,b in [(i,i),(i,i+1)]:
	    		while a >= 0 and b < L and s[a] == s[b]: a -= 1; b += 1
	    		r += (b-a)//2
	    return r


        # L gets the length of the string
        # r stores the count of palindromic substrings
        # loop through each character
        # for each character, expand around odd-length and even-length palindromes
        # expand around centre
        # count how many palindromes were found during the "expansion"
        # "i" is the index of the current character in the string s
        # (a,b) is the centre of possible palindromes
        # (i, i) odd length palindromes
        # (i, i + 1) even length palindromes
        # a moves left and b moves right to grow the palindrome
        # if the end values are equal, expand further
