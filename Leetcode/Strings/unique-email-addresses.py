class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def parse(email):
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.',"")
            return f"{local}@{domain}"
        
        return len(set(map(parse, emails)))
        

        # initial plan
        # set conditions for . and + 
        # for ".", basically remove it
        # for "+", ignore all char after it
        # output the number of different emails

        # final solution
        # split local and domain
        # remove everything after the plus sign, [split]
        # remove all periods, [replace]
        # return the normalised email
        # return 'f' helps to embed variables into a string. 
        # map(parse, emails) apply parse function to every email. 
        # set(...) collect result to eliminate duplicates
        # len(...) return the count of unique normalised emails.