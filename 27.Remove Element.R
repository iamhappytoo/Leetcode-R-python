remove <- function(nums, val){
  if(length(nums)<=1){
    return(c(length(nums),nums))
  }
  pt = 1
  k=0
  len=length(nums)
  while(pt<len & (!is.na(nums[pt]))){
    if(nums[pt] != val){
      pt = pt + 1
      k = k +1 
    }else if(nums[pt] == val){
      nums[pt:(len-1)] = nums[(pt+1):len]
      nums[length(nums)] = NA
    }else if(is.na(nums[pt])){
      pt = pt + 1
    }
  }
  if(!is.na(nums[pt]) & (nums[pt]==val)){  ##Here I forgot to do !is.na(nums[pt] check)
    nums[pt]=NA
  }
  return(c(k, nums))
}

nums=c(0,1,2,2,3,0,4,2)
val=2

remove(nums,val)


