/*
Problem: sort-vowels-in-a-string
Language: python3
Runtime: 2864 ms
Memory: 27.9 MB
Status: Accepted
*/

class Solution:
    def sortVowels(self, s: str) -> str:
        a = "aeiouAEIOU"
        x = []
        j = []
        for i in range(len(s)):
            if s[i] in a:
                j.append(s[i])
                x.append([])
            else:
                x.append([s[i]])
        j = sorted(j)
        for i in range(len(s)):
            if len(x[i]) == 0:
                x[i] = j[0]
                j.remove(j[0])
        c = ""
        for i in range(len(x)):
            c += x[i][0]
        return c
