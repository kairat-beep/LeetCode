class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        if len(temperatures) < 2:
            return [0]

        waitDaysStack = [(temperatures[0], 0)]
        waitDays = [0] * len(temperatures)

        for index, val in enumerate(temperatures[1:], 1):
            while len(waitDaysStack) and waitDaysStack[-1][0] < val:
                waitDays[waitDaysStack[-1][1]] = index - waitDaysStack[-1][1] 
                waitDaysStack.pop()
            waitDaysStack.append((val,index))

        return waitDays
