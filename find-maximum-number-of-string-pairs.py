/*
Problem: find-maximum-number-of-string-pairs
Language: python3
Runtime: 0 ms
Memory: 17.8 MB
Status: Accepted
*/

class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        count = 0
        x = []
        x.extend(words)
        for i in words:
            x.remove(i)
            if i[::-1] in x:
                count += 1
        return count
