/*
Problem: subtract-the-product-and-sum-of-digits-of-an-integer
Language: python3
Runtime: 0 ms
Memory: 17.6 MB
Status: Accepted
*/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        mul = 1
        sub = 0
        for i in str(n):
            mul *= int(i)
            sub += int(i)
        return mul - sub
