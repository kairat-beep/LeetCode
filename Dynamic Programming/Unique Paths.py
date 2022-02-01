class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        row = [1]*n
        for _ in range(m-1):
            for i in range(1, n):
                row[i] += row[i-1]
        return row[-1]