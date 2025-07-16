/*
Problem: number-of-arithmetic-triplets
Language: python3
Runtime: 8241 ms
Memory: 153.2 MB
Status: Accepted
*/

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        x = len(nums)
        a = []
        for i in range(x):
            for j in range(1,x):
                for k in range(2,x):
                    if i<j<k:
                        a.append([i,j,k])
        count = 0
        for i in a:
            if nums[i[2]]-nums[i[1]] == diff:
                if nums[i[1]]-nums[i[0]] == diff:
                    count += 1
        return count

    
