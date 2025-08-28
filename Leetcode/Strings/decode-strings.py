class Solution(object):
    def decodeString(self, s):
        stack = []; curNum = 0; curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curString = ''
                curNum = 0
            elif c == ']':
                num = stack.pop()
                prevString = stack.pop()
                curString = prevString + num*curString
            elif c.isdigit():     # curNum*10+int(c) is helpful in keep track of more than 1 digit number
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString
        


        # initial plan
        # expand the inner bracket, then the outer one
        
        # final solution 
        # stack to store previouos strings and numbers
        # curNum to build the number before brackets. 
        # curString to accumulate characters that are being built
        # if c is '[', push string and number to the stack
        # if c is ']', pop the last number and previous string
        # if c is a digit, build the full numbers
        # if c is a letter, add the char to curString