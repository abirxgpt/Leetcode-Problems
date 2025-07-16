/*
Problem: find-common-elements-between-two-arrays
Language: python3
Runtime: 19 ms
Memory: 17.7 MB
Status: Accepted
*/

class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x = 0
        y = 0
        for i in nums1:
            if i in nums2:
                x += 1
        for i in nums2:
            if i in nums1:
                y += 1
        return [x,y]
