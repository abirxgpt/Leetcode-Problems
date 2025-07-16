/*
Problem: minimum-average-of-smallest-and-largest-elements
Language: python3
Runtime: 0 ms
Memory: 17.6 MB
Status: Accepted
*/

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        ave = []
        x = sorted(nums)
        for i in range(0,len(x)//2):
            ave.append((x[0]+x[-1])/2)
            del x[0]
            del x[-1]
        y = sorted(ave)
        return y[0]
