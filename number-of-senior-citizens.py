/*
Problem: number-of-senior-citizens
Language: python3
Runtime: 3 ms
Memory: 17.9 MB
Status: Accepted
*/

class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in details:
            if 60 < int(i[11:13]):
                count += 1
        return count
