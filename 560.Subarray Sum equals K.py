class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mymap = {}
        cumsum = 0
        i = 0
        cnt = 0
        while i < len(nums):
            cumsum += nums[i]
            if cumsum == k:
                cnt += 1
            cnt += mymap.get(cumsum-k,0)
            mymap[cumsum] = mymap.get(cumsum,0) + 1
            i += 1
        return cnt
      
      
#Disregard sliding window suggestion, because the problem states negative values are possible (which discounts the use of sliding window).

