class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 递归法
        # if m == 1 or n == 1:
            # return 1
        # else:
            # return self.uniquePaths(m-1,n)+self.uniquePaths(m,n-1)
        # 动态规划
        result = []
        for i in range(n):
            row = []
            for j in range(m):
                if i == 0 or j == 0:
                    row.append(1)
                else:
                    row.append(result[i-1][j] + row[-1])
            result.append(row)
        return result[-1][-1]
