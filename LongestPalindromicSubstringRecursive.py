class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.max= 1
        self.maxTuple = (0,0)
        self.s=s
        self.multiDim = [ [None] * len(s) for _ in range (len(s))]
        for i in range(len(s)):
            self.multiDim[i][i] = 1
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if (self.multiDim[i][j] is None):
                    self.find(i,j)
        (start,end) = self.maxTuple
        return self.s[start:end+1]
    def find(self,i:int,j:int):
        if i>j or j >=len(self.s):
            return
        if j - i <= 2:
            self.multiDim[i][j]= j-i+1 if self.s[i]==self.s[j] else 0
            self.__updateMax__(i,j)
            return
        if self.multiDim[i+1][j-1] is None:
            self.find(i+1,j-1)
        if self.multiDim[i+1][j-1] ==0:
            self.multiDim[i][j] = 0
            return
        if self.multiDim[i+1][j-1] == j-1  - (i+1)+1 and self.s[i]==self.s[j]:
            self.multiDim[i][j] = 2 + self.multiDim[i+1][j-1]
            self.__updateMax__(i,j)
    def __updateMax__(self,i,j):
        if self.max < self.multiDim[i][j]:
            self.max = self.multiDim[i][j] 
            self.maxTuple = (i,j)

