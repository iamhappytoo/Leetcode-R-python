removeinvalid <- function(string){
  ##Remove the ) until reach the ( as beginning
  strarr=unlist(strsplit(string,split=''))
  i=1
  torm=NULL
  while(strarr[i]!='('){
    if(strarr[i]==')'){
      torm=c(torm,i)
      i=i+1
    }
  }
  if(length(torm)){
    strarr=strarr[-torm]
  }
  len=length(strarr)
  torm=NULL
  stack=NULL
  for(i in 1:len){
    if(strarr[i]=="("){
      stack=c(stack,strarr[i])
    }else if(strarr[i]==")"){
      if(length(stack)==0){
        torm=c(torm,strarr[i])
      }else{
        stack=stack[-1]
      }
    }
  }
  numbegin=length(stack)
  numend=length(torm)
  indbegin=which(strarr=="(")
  indend=which(strarr==")")
  rmbegin=getrmbegin(numbegin,indbegin)
  rmend=getrmend(numend,indend)
  output=NULL
  rmind=as.array(merge(rmbegin,rmend))
  for(i in 1:nrow(rmind)){
    if(nrow(rmind)>1){
      outstr=paste0(strarr[-rmind[i,]],collapse='')
    }else{
      outstr=paste0(strarr[-rmind[i]],collapse='')
    }
    output=c(output,outstr)
  }
  return(unique(output))
}
merge <- function(rmbegin,rmend){
  if(length(rmbegin)==0){
    return(rmend)
  }
  if(length(rmend)==0){
    return(rmbegin)
  }
  output=NULL
  for(i in 1:nrow(rmbegin)){
    for(j in 1:nrow(rmend)){
      output=rbind(output,c(rmbegin[i,],rmend[j,]))
    }
  }
  return(output)
}
getrmbegin <- function(numbegin,indbegin){
  rmbegin=NULL
  if(numbegin){
    if(length(indbegin)==numbegin){
      rmbegin=indbegin
    }
    if((length(indbegin)-numbegin)==1){
      rmbegin=indbegin[2:length(indbegin)]
    }
    if((length(indbegin)-numbegin)>1){
      lenbg=length(indbegin)
      for(i in lenbg:(1+numbegin)){
        rmbegin=rbind(rmbegin,indbegin[i:(i-numbegin+1)])
      }
    }
  }
  return(rmbegin)
}
getrmend <- function(numend,indend){
  rmend=NULL
  if(numend){
    if(length(indend)==numend){
      rmend=indend
    }
    if(length(indend)-numend){
      lened=length(indend)
      for(i in 1:(lened-numend)){
        rmend=rbind(rmend,indend[i:(i+numend-1)])
      }
    }
  }
  return(rmend)
}

s = "()())()"
removeinvalid(s)
