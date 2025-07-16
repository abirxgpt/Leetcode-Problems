/*
Problem: merge-strings-alternately
Language: python3
Runtime: 33 ms
Memory: 17.6 MB
Status: Accepted
*/

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) > len(word2):
            j = ""
            for i in range(len(word2)):
                j += word1[i]
                j += word2[i]
            j += word1[i+1:]
        elif len(word1) < len(word2):
            j = ""
            for i in range(len(word1)):
                j += word1[i]
                j += word2[i]
            j += word2[i+1:]
        else:
            j = ""
            for i in range(len(word1)):
                j += word1[i]
                j += word2[i]
        return j

