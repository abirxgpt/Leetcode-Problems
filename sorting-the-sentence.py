/*
Problem: sorting-the-sentence
Language: python3
Runtime: 34 ms
Memory: 17.6 MB
Status: Accepted
*/

class Solution:
    def sortSentence(self, s: str) -> str:
        x = s.split()
        y = [[]]*len(x)
        for i in x:
            y[int(i[-1])-1] = i[:-1]
        j = ""
        for i in y:
            j += i + " "
        return j[:-1]
