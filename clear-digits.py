/*
Problem: clear-digits
Language: python3
Runtime: 11 ms
Memory: 17.8 MB
Status: Accepted
*/

class Solution:
    def clearDigits(self, s: str) -> str:
        
        while s.isalnum() and not s.isalpha() and not s.isdigit():
            x = s
            already_found = False
            for i in range(len(s)):
                if s[i].isnumeric() and not already_found:
                    already_found = True
                    x = s[:i-1] + s[i:]
                    x = x[:i-1] + x[i:]
            s = x
        return s

