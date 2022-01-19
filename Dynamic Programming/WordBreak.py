from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.longestSubString = 0
        reachable = [None] * (len(s) + 1)
        reachable[0] = 1
        for i in wordDict:
            self.longestSubString = max(self.longestSubString, len(i))
        i = 0 
        while i < len(s):
            if not reachable[i]:
                i += 1
                continue
            reached = self.compare(s, i , wordDict)
            for j in reached:
                reachable[j] = 1
            i += 1
        return reachable[-1]
    
    def compare(self,s , position, wordDict):
        newWord = s[position : self.longestSubString + position]
        sizes = set()
        for i in wordDict:
            if newWord.startswith(i):
                sizes.add(position + len(i))
        return list(sizes)

Solution().wordBreak("leetcode",["leet","code"])