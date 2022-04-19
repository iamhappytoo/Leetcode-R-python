class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == len(nums1):
            return nums1
        if m == 0:
            nums1[0:(n+1)] = nums2
            return nums1
        
        pt0 = m + n - 1
        pt1 = m - 1
        pt2 = n - 1
        while pt2 > -1 and pt1 > -1:
            if nums1[pt1] <= nums2[pt2]:
                nums1[pt0] = nums2[pt2] 
                pt2 -= 1
                pt0 -= 1
            else:
                nums1[pt0] = nums1[pt1]
                pt1 -= 1
                pt0 -= 1
        if pt2 > -1:        
            nums1[0:(pt2+1)]=nums2[0:(pt2+1)]
        return nums1
      
  ###Cleaner version
  class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1
    
        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
          if p2 < 0:
            break
          if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
          else:
            nums1[p] = nums2[p2]
            p2 -= 1
            
