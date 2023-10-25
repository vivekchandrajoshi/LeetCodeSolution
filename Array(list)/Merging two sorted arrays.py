from typing import List


# https://leetcode.com/problems/merge-sorted-array/
# Brute Force Approach
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(0,n):
            nums1[m+i] = nums2[i]
        nums1.sort()

# Time complexity:
# O((m+n)log(m+n))
# Due to sort func
#
# Space complexity:
# O(1)
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
ob1 = Solution()
ob1.merge(nums1, m, nums2, n)
print(nums1)


class Solution1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        arr3 = [None] * (m + n)
        i = 0
        j = 0
        k = 0
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                arr3[k] = nums1[i]
                k = k + 1
                i = i + 1
            else:
                arr3[k] = nums2[j]
                k = k + 1
                j = j + 1

        while i < m:
            arr3[k] = nums1[i]
            k = k + 1
            i = i + 1
        while j < n:
            arr3[k] = nums2[j]
            k = k + 1
            j = j + 1
        return arr3

# Time Complexity : O(m + n)
# Space Complexity : O(m + n)

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
ob1 = Solution1()
print(ob1.merge(nums1, m, nums2, n))
