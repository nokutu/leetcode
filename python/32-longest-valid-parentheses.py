import time


class Solution:
    def longestValidParentheses(self, text: str) -> int:
        text = text.lstrip(')').rstrip('(')

        total_left = text.count('(')
        total_right = text.count(')')
        diff = total_left - total_right

        best = 0

        i = 0
        j = len(text) - 1

        while i < len(text):
            max_level = 0
            level = 0
            any_right = False

            for k in range(i, j + 1):
                c = text[k]
                if c == '(':
                    level += 1
                elif c == ')':
                    level -= 1
                    any_right = True

                if level == 0:
                    best = max(best, k - i + 1)
                elif level < 0:
                    i = k
                    break

                if level > max_level and not any_right:
                    max_level = level

            if max_level > total_right:
                i += max_level - total_right
            else:
                i += 1
        return best


start = time.time()
print(Solution().longestValidParentheses("(((((((((((((((((())"))
end = time.time()
print(end - start)
