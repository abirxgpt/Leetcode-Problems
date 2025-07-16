/*
Problem: rings-and-rods
Language: python3
Runtime: 0 ms
Memory: 17.7 MB
Status: Accepted
*/

class Solution:
    def countPoints(self, rings: str) -> int:
        count = 0
        s = [[],[],[],[],[],[],[],[],[],[]]
        for i in range(0,len(rings),2):
            s[int(rings[i+1])].append(rings[i])
        for i in range(len(s)):
            if "B" in s[i] and "G" in s[i] and "R" in s[i]:
                count += 1
        return count



