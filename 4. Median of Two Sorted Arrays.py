class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1+nums2
        nums.sort()
        leng = len(nums)
        if leng % 2 == 0:
            return (nums[leng//2-1] + nums[leng//2])/2
        else:
            return nums[leng//2]
