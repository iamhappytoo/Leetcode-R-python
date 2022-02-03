sparsevector <- function(arr1,arr2){
  vector=NULL
  for(i in 1:length(arr1)){
    if((arr1[i]!=0)|(arr2[i]!=0)){
      vector=rbind(vector,c(arr1[i],arr2[i]))
    }
  }
  return(vector)
}
dotproduct <- function(vector){
  result=0
  for(i in 1:nrow(vector)){
    result=result+vector[i,1]*vector[i,2]
  }
  return(result)
}

arr1=c(0,0,1,0,2)
arr2=c(2,1,1,0,1)
dotproduct(sparsevector(arr1,arr2))
