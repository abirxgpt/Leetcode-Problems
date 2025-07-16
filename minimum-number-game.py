/*
Problem: minimum-number-game
Language: python3
Runtime: 0 ms
Memory: 18 MB
Status: Accepted
*/

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        x = sorted(nums)
        arr = []
        for i in range(0,len(x),2):
            arr.append(x[i+1])
            arr.append(x[i])
        return arr
