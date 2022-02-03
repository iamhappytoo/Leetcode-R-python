getcount<- function(arr,k){
  savesum=NULL
  sum=0
  sum=sum+arr[1]
  count=1
  countsumk=0
  savesum=array(c(sum,count),dim=c(1,2))
  for(i in 2:length(arr)){
    sum=sum+arr[i]
    ind=which(savesum[,1]==sum)
    if(length(ind)>0){
      savesum[ind,2]=savesum[ind,2]+1
    }else{
      savesum=rbind(savesum,c(sum,1))
    }
    if(sum==k){
      countsumk=countsumk+1
    }else{
      if((sum-k)%in%savesum[,1]){
        countsumk=countsumk+1
      }
    }
  }
  return(countsumk)
}
arr=c(1,1,1)
k=2
getcount(arr,k)