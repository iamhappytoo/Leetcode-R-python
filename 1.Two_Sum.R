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
