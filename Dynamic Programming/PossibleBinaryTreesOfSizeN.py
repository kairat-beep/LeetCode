class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.d = dict()
        self.d[0]=1
        self.d[1]=1
        self.d[2]=2
        self.d[3]=5
        self.helper(n)
        return self.d[n]
    def helper(self,n):
        if n in self.d:
            return self.d[n]
        accumulate = 0
        for i in range(1,n+1):
            left = self.helper(i  - 1)
            right = self.helper(n - i)
            accumulate += left * right
        self.d[n] = accumulate
        return accumulate