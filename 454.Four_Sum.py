class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        hashA = {}
        hashB = {}
        n = len(nums1)
        for i in range(n):
            for j in range(n):
                SumA = nums1[i]+nums2[j]
                SumB = nums3[i]+nums4[j]
                hashA[SumA] = hashA.get(SumA,0) + 1
                hashB[SumB] = hashB.get(SumB,0) + 1
        
        count = 0
        for key in hashA:
            complement = 0 - key
            if complement in hashB:
                count += hashA[key] * hashB[complement]
                
        return count
