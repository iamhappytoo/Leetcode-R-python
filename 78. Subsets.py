##Cascade method
class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    
    output = [[]]
    for num in nums:
      output += [curr + [num] for curr in output]
      
    return output
  
##Backtracking
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        if not nums or len(nums) == 0:
            return results
        nums.sort()
        length = len(nums)
        subset = []
        def subsetsHelper(startIndex):
            ##deep copy subset & put in results
            results.append(subset.copy())
            
            for i in range(startIndex, length):
                subset.append(nums[i])
                subsetsHelper(i + 1)
                subset.pop()
                
        subsetsHelper(0)
        
        return results
##Change the usage of local function into global function with the usage of self and the transfer of parallel self function parameters to the input
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        if not nums or len(nums) == 0:
            return results
        nums.sort()
        length = len(nums)
        subset = []
        self.subsetsHelper(nums, 0, subset, results, length)
        
        return results
    def subsetsHelper(self, nums, startIndex, subset, results, length):
            ##deep copy subset & put in results
            results.append(subset.copy())
            
            for i in range(startIndex, length):
                subset.append(nums[i])
                self.subsetsHelper(nums, i + 1, subset, results, length)
                subset.pop()
##This is much quicker than the usage of local function.                
