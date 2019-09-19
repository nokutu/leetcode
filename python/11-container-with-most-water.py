from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        def f(i: int, j: int):
            if i == j:
                return 0

            v_i = height[i]
            v_j = height[j]

            if v_i > v_j:
                return max(f(i, j - 1), v_j * (j - i))
            else:
                return max(f(i + 1, j), v_i * (j - i))

        return f(0, len(height) - 1)


print(Solution().maxArea([8, 2, 2, 100, 1, 8]))
