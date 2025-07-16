/*
Problem: kth-distinct-string-in-an-array
Language: python3
Runtime: 147 ms
Memory: 17.9 MB
Status: Accepted
*/

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for i in arr:
            if arr.count(i) == 1:
                k -= 1
                if k == 0:
                    return i
        return ""
