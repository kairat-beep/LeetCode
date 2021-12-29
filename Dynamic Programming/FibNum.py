class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        if n <= 2:
            return 1
        a, b = 1, 1
        for i in range(n-2):
            a, b= b, a + b
        return b