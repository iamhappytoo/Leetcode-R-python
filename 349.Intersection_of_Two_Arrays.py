class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seta = set()
        setb = set()
        for i in nums1:
            seta.add(i)
        for j in nums2:
            setb.add(j)
            
        return seta.intersection(setb)
