from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a= set()
        for i in nums1:
            for j in nums2:
                if i == j:
                    a.add(i)
                    break
        return a

# Time complexity : O(N^2)
# Space complexity : O(n+m)

nums1 = [1,2,2,1]
nums2 = [2,2]
ob1 = Solution()
print(ob1.intersection(nums1, nums2))

class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)
# Time complexity : O(m*n)
# Space complexity : O(n+m)

nums1 = [1,2,2,1]
nums2 = [2,2]
ob1 = Solution1()
print(ob1.intersection(nums1, nums2))

class Solution2:
    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)

# Time complexity : O(m+n)
# Space complexity : O(n+m)

nums1 = [1,2,2,1]
nums2 = [2,2]
ob1 = Solution2()
print(ob1.intersection(nums1, nums2))