values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

before = {
    'I': ['V', 'X'],
    'X': ['L', 'C'],
    'C': ['D', 'M'],
}

class Solution:
    def romanToInt(self, text: str) -> int:
        s = 0
        idx = 0
        while idx < len(text):
            value = values[text[idx]]

            if idx < len(text)-1 and text[idx] in before and text[idx+1] in before[text[idx]]:
                s += values[text[idx+1]] - value
                idx += 2
            else:
                s += value
                idx += 1
        return s

print(Solution().romanToInt('IV'))
