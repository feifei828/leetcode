class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        start = '1'
        if n == 1:
            return start
        while n > 1:
            count = 0
            s = ''
            new_start = ''
            for i in start:
                if i != s and count > 0:
                    new_start += str(count) + s
                    count = 0
                s = i
                count += 1
            if count > 0:
                new_start += str(count) + s
            start = new_start
            n -= 1
        return start
