/*
Problem: number-of-changing-keys
Language: python3
Runtime: 0 ms
Memory: 17.4 MB
Status: Accepted
*/

class Solution:
    def countKeyChanges(self, s: str) -> int:
        s = s.lower()
        k = ''
        change = -1
        for i in s:
            if k != i:
                change += 1
            k = i
        return change

