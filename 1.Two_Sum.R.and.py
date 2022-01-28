twosum <- function(nums,target){
  len=length(nums)
  n=1
  idxMap=NULL
  while(TRUE){
    if(!(target-nums[n])%in%idxMap){
      idxMap=rbind(idxMap,c(nums[n],n))
      n=n+1
    }else{
      return(c(idxMap[which(idxMap[,1]==(target-nums[n])),2],n)-1)
    }
  }
}

nums=c(3,2,4)
target=6
twosum(nums,target)
####Python O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i in range(len(nums)):
            mydict[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in mydict and mydict[complement] != i:
                return [i, mydict[complement]]
###Python O(n2)
class Solution:
  def twoSum(self, nums, target):
    for i in range(len(nums)):
      for j in range(i+1, len(nums)):
        if nums[i]+nums[j] == target:
          return [i,j]
                  
