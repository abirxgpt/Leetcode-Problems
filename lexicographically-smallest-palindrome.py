/*
Problem: lexicographically-smallest-palindrome
Language: python3
Runtime: 58 ms
Memory: 18.1 MB
Status: Accepted
*/

class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        if len(s)%2==0:
            k = len(s) // 2
            a = list(s[:k])
            b = s[k:]
            b = list(b[::-1])
            for i in range(k):
                if a[i] != b[i]:
                    if a[i] > b[i]:
                        a[i] = b[i]
                    elif a[i] < b[i]:
                        b[i] = a[i]
            j = ""
            for i in range(k):
                j += a[i]
            for i in range(k-1,-1,-1):
                j += b[i]
            return j
        else:
            k = len(s) // 2
            a = list(s[:k])
            b = s[k+1:]
            b = list(b[::-1])
            for i in range(k):
                if a[i] != b[i]:
                    if a[i] > b[i]:
                        a[i] = b[i]
                    elif a[i] < b[i]:
                        b[i] = a[i]
            j = ""
            for i in range(k):
                j += a[i]
            j += s[k]
            for i in range(k-1,-1,-1):
                j += b[i]
            return j

