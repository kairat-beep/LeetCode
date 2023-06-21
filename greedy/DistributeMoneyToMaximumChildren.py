class Solution:
    def distMoney(self, money: int, children: int) -> int:
        if money < children :
            return -1
        distributed = 0
        origM = money
        #don't leave empty handed
        money -= children

        #split the rest uneven to fill 8
        distributed += money /7
        if distributed > children:
            return children - 1

        if money % 7 == 3:
            if int(distributed) == children - 1:
                return max(0,children  - 2)
        return max(0,int(distributed))

