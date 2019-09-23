from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = {''}

        for i in range(n):
            next_ret = set()
            for s in ret:

                for x in range(i+1):
                    for y in range(x, i+1):
                        next_ret.add(s[:x] + '(' + s[x:y] + ')' + s[y:])

            ret = next_ret

        return list(ret)


print(Solution().generateParenthesis(3))
