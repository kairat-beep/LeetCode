class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            horizontal_check = [_  for _ in board[i]   if _ !='.']
            if (len(horizontal_check) != len(set(horizontal_check))):
                return False
        for i in range(9):
            vertical_check = [_[i]  for _ in board if _[i] != '.']
            if (len(vertical_check) != len(set(vertical_check))):
                return False
        for i,j in ((0,0),(0,3),(0,6),
                    (3,0),(3,3),(3,6),
                    (6,0),(6,3),(6,6)):
            if not self.__qube_check(board,i,j):
                return False
        return True
    def __qube_check(self,board,y,x):
        block = []
        for i in board[y:y+3]:
            block.extend(_ for _ in i[x:x+3] if _ != '.')
        print (block)
        return len(block) == len(set(block))


