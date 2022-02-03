getkthlargest <- function(arr,k){
  ##quickselect algorithm##
  if(length(arr)==0){
    return(NULL)
  }
  if(max(arr)==min(arr)){
    return(arr[1])
  }
  n=length(arr)
  start=1
  end=n
  curend=n+1
  while(curend!=(n-k+1)){ ##move smallest left to pivot in quickselect
    curstart=start; curend=end
    while(arr[curend]==arr[curstart]){
      curend=curend-1
      curstart=curstart-1
      n=n-1
    }
    pivot_index=curstart+floor((curend-curstart)/2)
    pivot=arr[pivot_index]
    while(curstart < curend){
      if(arr[curstart]<pivot){
        curstart=curstart+1
      }else{
        temp=arr[curend]
        arr[curend]=arr[curstart]
        arr[curstart]=temp
        curend=curend-1
      }
    }
    if(arr[curend]<pivot){
      curend=curend+1
    }
    if(curend<(n-k+1)){
      start=curend
    }else{
      end=curend-1
    }
  }
  print(arr)
  print(pivot)
  return(pivot)
}
arr=c(3,3,3,3,3,3,3)
print(getkthlargest(arr,4))
