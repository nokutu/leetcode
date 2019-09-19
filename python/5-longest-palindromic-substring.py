class Solution:
    def longestPalindrome(self, text: str) -> str:
        def f(i: int, j: int):
            if i >= 0 and j < len(text) and text[i] == text[j]:
                ret = f(i - 1, j + 1)
            else:
                ret = (i+1, j-1)
            return ret

        max_size = 0
        max_str = ""
        for idx in range(len(text)):
            i, j = f(idx-1, idx+1)
            size = j-i+1

            if size > max_size:
                max_size = size
                max_str = text[i:j+1]

            i, j = f(idx, idx+1)
            size = j-i+1

            if size > max_size:
                max_size = size
                max_str = text[i:j+1]
        return max_str


print(Solution().longestPalindrome('aabbbba'))