class Solution:
    def longestPalindrome(self, s: str) -> str:
        maximum= 1
        maxTuple = (0,0)
        multiDim = [ [None] * len(s) for _ in range (len(s))]
        for i in range(len(s)):
            multiDim[i][i] = 1

        for i in range(len(s)-1):
            multiDim[i][i+1]=2 if s[i] == s[i+1] else 0
            maxTuple= (i,1+i) if s[i] ==s[i+1] else maxTuple 

        for col in range(2, len(s)):
            for row  in range(0,col - 1):
                if multiDim[row][col] is None:
                    if multiDim[row+1][col-1] != 0 and s[row]==s[col]:
                        multiDim[row][col] = 2 + multiDim[row+1][col-1]
                        if(maximum<multiDim[row][col]):
                            maxTuple = (row,col)
                            maximum = multiDim[row][col]
                    else:
                        multiDim[row][col] = 0

        (start,end) = maxTuple
        return s[start:end+1]
