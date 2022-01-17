###Hash table###
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        mydict = {}
        for num in nums:
            if num in mydict:
                return True
            mydict[num]=1
        return False
###Unique###
dupli <- function(nums){
    uniq=unique(nums)
    if(length(uniq) == length(nums)){
      return(FALSE)
    }else{
      return(TRUE)
    }
}
###Sort###
dupli <- function(nums){
    nums=sort(nums)
    for(i in 1:(length(nums)-1)){
        if(nums[i]==nums[i+1]){
            return(TRUE)
        }
    }
    return(FALSE)
}
   
