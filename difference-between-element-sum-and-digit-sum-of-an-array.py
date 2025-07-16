/*
Problem: difference-between-element-sum-and-digit-sum-of-an-array
Language: python3
Runtime: 23 ms
Memory: 17.9 MB
Status: Accepted
*/

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        x = 0
        y = 0
        for i in nums:
            x += i
            for j in str(i):
                y += int(j)
        return abs(x-y)
