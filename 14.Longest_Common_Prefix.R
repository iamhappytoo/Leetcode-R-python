##Time cost: 15min from speaking, coding to testing. 3 bugs remaining. line 24: cp should be cparr. 

LCP <- function(strlist){
  if(length(strlist)==1){
    return(strlist[1])
  }
  CP=strlist[1]
  for(i in 2:length(strlist)){
    CP=cp(CP,strlist[i])
  }
  return(paste(CP,collapse=''))
}

cp <- function(CP,str){
  cparr=unlist(strsplit(CP,split=''))
  strarr=unlist(strsplit(str,split=''))
  if((length(cparr)==0) | (length(strarr)==0) | (cparr[1]!=strarr[1])){
    return('')  
  }
  i=1
  while((i <=length(cparr)) & (i<=length(strarr)) & (cparr[i]==strarr[i])){
    i=i+1
  }
  return(cparr[1:(i-1)])
}

str=c('flower','flow','flight')
LCP(str)
