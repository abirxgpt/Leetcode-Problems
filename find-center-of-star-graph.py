/*
Problem: find-center-of-star-graph
Language: python3
Runtime: 0 ms
Memory: 45.5 MB
Status: Accepted
*/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        x = edges[0]
        num1 = x[0]
        num2 = x[1]
        if num1 in edges[1]:
            return num1
        else:
            return num2
            


