class Solution:
    def isMatch(self, text: str, expr: str) -> bool:
        len_text = len(text)
        len_expr = len(expr)

        cache = {}
        
        def f(i: int, j: int):
            if (i, j) in cache:
                return cache[i, j]

            if len_text == i or len_expr == j:
                while len_expr > j + 1 and expr[j+1] == '*':
                    j += 2
                
                ret = len_text == i and len_expr == j
            else:
                c = text[i]
                match = expr[j]
                star = len_expr > j + 1 and expr[j+1] == '*'

                if star:
                    if match != '.' and match != c:
                        ret = f(i, j+2)
                    else:
                        ret = f(i+1, j) or f(i, j+2)
                else:
                    if match != '.' and match != c:
                        ret = False
                    else:
                        ret = f(i+1, j+1)
            cache[(i, j)] = ret
            return ret

        return f(0, 0)
        

print(Solution().isMatch("aa", "a.*b"))