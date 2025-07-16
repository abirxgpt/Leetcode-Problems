/*
Problem: number-of-strings-that-appear-as-substrings-in-word
Language: python3
Runtime: 4 ms
Memory: 17.8 MB
Status: Accepted
*/

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for i in patterns:
            if i in word:
                count += 1
        return count
