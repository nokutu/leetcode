digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
signs = ['-', '+']

max_val = 2 ** 31 - 1
min_val = -2 ** 31


class Solution:
    def myAtoi(self, text: str) -> int:
        text = text.strip()

        for idx, c in enumerate(text):
            if c not in digits + signs:
                text = text[:idx]

        if len(text) == 0 or text[0] not in digits + signs:
            return 0

        mult = 1
        if text[0] in signs:
            if text[0] == '-':
                mult = -1
            text = text[1:]

        sum = 0
        for idx, c in enumerate(text):
            if c not in digits:
                sum = sum // 10 ** (len(text) - idx)
                break
            dig = 10 ** (len(text) - idx - 1)
            val = ord(c) - ord('0')
            sum += dig * val

        ret = sum * mult

        if ret > max_val:
            return max_val
        elif ret < min_val:
            return min_val

        return ret


print(Solution().myAtoi("-50-asdfa"))
