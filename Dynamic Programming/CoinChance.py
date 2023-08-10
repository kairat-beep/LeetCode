class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        setCoins = set(coins)
        coins.sort()
        initSteps = [0] * (amount + 1)
        for c in [i for i in coins if i<=amount]:
            initSteps[c] = 1
        for i in range(min(coins), amount+1):
            if i in setCoins:
                continue
            jumps = [ 1+initSteps[i-j] for j in coins if i >= j and initSteps[i-j] != 0]
            if len(jumps):
                initSteps[i] =  min(jumps)
        return -1 if initSteps[amount]==0 else initSteps[amount]
