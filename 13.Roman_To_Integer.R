romantointeger <- function(s){
  
  sarr=unlist(strsplit(s,split=''))
  i=1; total=0
  while(i <= length(sarr)){
    j=i+1
    if(j<=length(sarr) & (value(sarr[i])<value(sarr[j]))){
      total=total+value(sarr[j])-value(sarr[i])
      i=i+2
    }else{
      total=total+value(sarr[i])
      i=i+1
    }
  }
  return(total)
}
value <- function(s){
  if(s=='M'){return(1000)}
  if(s=='D'){return(500)}
  if(s=='C'){return(100)}
  if(s=='L'){return(50)}
  if(s=='X'){return(10)}
  if(s=='V'){return(5)}
  if(s=='I'){return(1)}
  else{return(0)}
}
romantointeger('MCMXCIV')

romantoInt <- function(s){
  sarr=unlist(strsplit(s,split=''))
  total=value(sarr[length(sarr)])
  for(i in (length(sarr)-1):1){
    if (value(sarr[i])<value(sarr[i+1])){
      total=total-value(sarr[i])
    }else{
      total=total+value(sarr[i])
    }
  }
  return(total)
}
