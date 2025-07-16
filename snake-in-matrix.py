/*
Problem: snake-in-matrix
Language: python3
Runtime: 3 ms
Memory: 18 MB
Status: Accepted
*/

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        matrix = [[i * n + j for j in range(n)] for i in range(n)]
        u = 0
        v = 0
        for i in commands:
            if i == "DOWN":
                u += 1
            elif i == "UP":
                u -= 1
            elif i == "RIGHT":
                v += 1
            elif i == "LEFT":
                v -= 1
        return matrix[u][v]
