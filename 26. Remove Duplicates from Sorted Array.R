removeduplicates <- function(nums){
  if(length(nums)<=1){
    return(c(length(nums),nums))
  }
  pt = 1
  k=0
  len=length(nums)
  while(pt<len & (!is.na(nums[pt+1]))){ ##Here I forgot to include is.na(nums[pt+1]) in this loop. 
    if(nums[pt] == nums[pt+1]){
      val=nums[pt]
      maxps=max(which(nums == val))
      if(maxps<len){
        nums[(pt+1):(len-(maxps-pt))]=nums[(maxps+1):len] ##Be careful with this maxps terms
        nums[((len-(maxps-pt))+1):len]=NA
      }else{
        nums[(pt+1):len]=NA
      }
    }
    k = k + 1
    pt = pt + 1
  }
  return(c(k+1, nums))
}

nums=c(0,0,1,1,1,2,2,3,3,4)
removeduplicates(nums)

removeduplicates <- function(nums){
  if(length(nums) <=  1){
      return(length(nums))
  }
  i = 1
  j = 2
  while(j <= length(nums)){
    if(nums[j] != nums[i]){
      i=i+1
      nums[i]=nums[j]
    }
    j= j+1
  }
  return(i)
}
