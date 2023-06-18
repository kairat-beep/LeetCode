class Solution:

    def mostPoints(self, questions: List[List[int]]) -> int:
        self.cache = dict()
        self.questions = questions
        self.helper(0)
        return self.cache[0]
    def helper(self,pos):
        if pos >= len(self.questions):
            return 0

        if pos in self.cache:
            return self.cache[pos]

        gain, wait = self.questions[pos]
        self.cache[pos] = max(gain + self.helper(pos + wait + 1), self.helper(pos + 1))
        return self.cache[pos]
