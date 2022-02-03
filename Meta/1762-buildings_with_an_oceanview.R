getoceanview <- function(arr){
  if(length(arr)==0){
    return(NULL)
  }else{
    output=length(arr)
    max=arr[length(arr)]
    for(i in (length(arr)-1):1){
      if(arr[i]>max){
        output=c(output,i)
        max=arr[i]
      }
    }
    return(rev(output)-1)
  }
}
arr=c(1,3,2,4)
getoceanview(arr)

##From left to right -- monotonic stack

getoceanview <- function(arr){
  stack=NULL
  answer=NULL
  stack=arr[1]
  answer=1
  for(i in 2:length(arr)){
    j=length(stack)
    while(j>0){
      if(stack[j]>arr[i]){
        break
      }else{
        stack=stack[-j]; 
        answer=answer[-j]; 
        j=j-1;
      }
    }
    stack=c(stack,arr[i])
    answer=c(answer,i)
  }
  return(answer-1)
}
arr=c(4,2,3,1)
getoceanview(arr)