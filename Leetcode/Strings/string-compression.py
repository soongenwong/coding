class Solution:
  def compress(self, chars: List[str]) -> int:
    ans = 0
    i = 0

    while i < len(chars):
      letter = chars[i]
      count = 0
      while i < len(chars) and chars[i] == letter:
        count += 1
        i += 1
      chars[ans] = letter
      ans += 1
      if count > 1:
        for c in str(count):
          chars[ans] = c
          ans += 1

    return ans
        


        # initial plan
        # find the first value, and count the number , return the number
        # move to the next value, count the number, return the number


        # final solution 
        # count occurences of first letter
        # output the letter
        # if the count is more than 1, output the count as well