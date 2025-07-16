/*
Problem: replace-all-digits-with-characters
Language: python3
Runtime: 0 ms
Memory: 17.7 MB
Status: Accepted
*/

class Solution:
    def replaceDigits(self, s: str) -> str:
        a = "abcdefghijklmnopqrstuvwxyz"
        j = ""
        for i in range(len(s)):
            if s[i].isalpha():
                j += s[i]
            else:
                x = a.index(s[i-1]) + int(s[i])
                j += a[x]
        return j

