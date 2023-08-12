class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        to_return = []
        current_stack = []
        def recursive(k, n, index):
            nonlocal to_return, current_stack
            if n == 0 and k == 0:
                to_return.append(current_stack.copy())
                return
            if n <= 0 or k <= 0 or n < index or index>9:
                return
            current_stack.append(index)
            recursive(k - 1, n - index, index + 1)
            current_stack.pop()
            recursive(k, n, index + 1)
        
        recursive(k, n, 1)
        print(to_return)
        return  to_return
