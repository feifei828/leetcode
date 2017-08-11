class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_val = 0
        for i in range(len(height)):
            for j in range(len(height) - i - 1):
                h = height[i] if height[i] < height[i + j + 1] else height[i + j + 1]
                val = h * (j + 1)
                if max_val < val:
                    max_val = val
        return max_val


class NewSolution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_val = 0
        i = 0
        j = len(height) - 1
        while i < j:
            if height[i] < height[j]:
                val = height[i] * (j - i)
                i += 1
            else:
                val = height[j] * (j - i)
                j -= 1
            if max_val < val:
                max_val = val
        return max_val
