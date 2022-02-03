solution <- function(arr){
  output=NULL
  for(i in 1:length(arr)){
    ind=i-1
    output=c(output,rep(ind,arr[i]))
  }
  return(output)
}
pickindex <- function(solute){
  return(sample(solute,1))
}
arr=c(1,3)
solute=solution(arr)
for(i in 1:7){
  print(pickindex(solute))
}

solution <- function(arr){
  cumsum=0
  cumsums=NULL
  for(i in 1:length(arr)){
    cumsum=cumsum+arr[i]
    cumsums=c(cumsums,cumsum)
  }
  return(c(cumsum,cumsums))
}
##29, 4,6,9,10
pickindex <- function(solute){
  cumsum=solute[1]
  cumsums=solute[2:length(solute)]
  target=sample(seq(1:cumsum),1)
  high=length(cumsums)
  low=1
  while(low<high){
    mid=floor((low+high)/2)
    if(cumsums[mid]<target){
      low=mid+1
    }else{
      high=mid
    }
  }
  return(low-1)
}
arr=c(1,3,5,7)
solute=solution(arr)
for(i in 1:8){
  print(pickindex(solute))
}

