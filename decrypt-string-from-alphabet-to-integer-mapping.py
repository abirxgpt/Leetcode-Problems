/*
Problem: decrypt-string-from-alphabet-to-integer-mapping
Language: python3
Runtime: 0 ms
Memory: 17.6 MB
Status: Accepted
*/

class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = []
        x = 0

        while x < len(s):
            if x + 2 < len(s) and s[x + 2] == '#':
                val = int(s[x: x + 2])
                ans.append(chr(val + 96))
                x += 3
            else:
                ans.append(chr(int(s[x]) + 96))
                x += 1

        return ''.join(ans)

