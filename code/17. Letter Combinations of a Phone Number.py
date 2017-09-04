class Solution(object):
    data = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }

    def create(self, l, d, s, index):
        if index == len(d):
            if s:
                l.append(s)
            return
        for i in self.data[d[index]]:
            self.create(l, d, s + i, index + 1)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = []
        self.create(res, digits, '', 0)
        return res
