from typing import List
import itertools
from functools import reduce


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        lists = []
        for c in digits:
            extra = 0
            num = int(c)

            if num == 7:
                lists.append([chr(97 + (num - 2) * 3), chr(97 + (num - 2) * 3 + 1), chr(97 + (num - 2) * 3 + 2),
                              chr(97 + (num - 2) * 3 + 3)])
            elif num == 8:
                lists.append([chr(97 + (num - 2) * 3 + 1), chr(97 + (num - 2) * 3 + 2), chr(97 + (num - 2) * 3 + 3)])
            elif num == 9:
                lists.append([chr(97 + (num - 2) * 3 + 1), chr(97 + (num - 2) * 3 + 2), chr(97 + (num - 2) * 3 + 3),
                              chr(97 + (num - 2) * 3 + 4)])
            else:
                lists.append([chr(97 + (num - 2) * 3 + 0), chr(97 + (num - 2) * 3 + 1), chr(97 + (num - 2) * 3 + 2)])

        return list(map(lambda s: reduce(lambda a, b: a + b, s, ''), itertools.product(*lists)))


print(Solution().letterCombinations('9'))
