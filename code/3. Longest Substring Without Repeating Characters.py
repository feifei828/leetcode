class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        r = 0
        w = 1
        max_length = 1 if s else 0
        while w < len(s):
            if s[w] not in s[r:w]:
                w += 1
                length = w - r
                if max_length < length:
                    max_length = length
            else:
                for i in range(w - r):
                    if s[r + i] == s[w]:
                        r = r + i + 1
                        break

        return max_length
