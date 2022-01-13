countbin <- function(s){
  arr=as.numeric(unlist(strsplit(s,split='')))
  savedict = NULL
  i=1
  count=1
  while(i <= (length(arr)-1)){
    if(arr[i+1] == arr[i]){
      count=count+1
    }else{
      savedict=c(savedict,count)
      count=1
    }
    i=i+1
  }
  savedict = c(savedict, count)
  if(length(savedict)<=1){
    return(0)
  }
  sumarr=0
  for(i in 1:(length(savedict)-1)){
      sumarr = sumarr + min(savedict[i],savedict[i+1])
  }
  return(sumarr)
}

linearscan <- function(s){
  arr=as.numeric(unlist(strsplit(s,split='')))
  prev=0
  cur=1
  ans=0
  for(i in 2:length(arr)){
      if(arr[i-1]!=arr[i]){
          ans = ans + min(prev, cur)
          prev = cur
          cur = 1
      }else{
          cur=cur+1
      }
  }
  return(ans + min(prev, cur))
}

s = "00110011"
countbin(s)
linearscan(s)
