class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(s) == 0 or len(p) == 0:
            while len(p) > 1 and p[1] == '*':
                p = p[2:]
            return len(s) == 0 and len(p) == 0

        c = s[0]
        match = p[0]
        star = len(p) > 1 and p[1] == '*'

        if star:
            if match != '.' and match != c:
                return self.isMatch(s, p[2:])
            else:
                return self.isMatch(s[1:], p) or self.isMatch(s, p[2:])
        else:
            if match != '.' and match != c:
                return False
            else:
                return self.isMatch(s[1:], p[1:])
        

print(Solution().isMatch("aa", ".*ab*"))