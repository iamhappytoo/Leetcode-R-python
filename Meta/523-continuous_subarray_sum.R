continSubarrSum <- function(nums, k){
  cumsum=0
  savemod=matrix(c(0,-1),ncol=2)
  for(i in 1:length(nums)){
    cumsum=cumsum+nums[i]
    mod = cumsum %% k
    if(mod %in% savemod[,1]){
      ind=min(savemod[which(savemod[,1]==mod),2])
      if((i-ind)>1){
        return(TRUE)
      }
    }else{
      savemod=rbind(savemod,c(mod,i))
    }
  }
  return(FALSE)
}

nums=c(23,2,4,6,6)
k=7
continSubarrSum(nums,k)