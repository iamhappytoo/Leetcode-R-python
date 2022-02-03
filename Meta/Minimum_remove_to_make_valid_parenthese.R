getvalid<- function(string){
  strarr=unlist(strsplit(string,split=''))
  saverm=NULL
  counter=0
  positive=NULL
  symbol=c("(",")")
  sign=c(1,-1)
  ss=cbind(symbol,sign)
  for (i in 1:length(strarr)){
    if(counter==0){
      if(strarr[i]==")"){
        saverm=c(saverm,i)
      }else if(strarr[i]=="("){
        counter=counter+1
        positive=c(positive,i)
      }
    }else{
      if(strarr[i]==")"){
        counter=counter-1
      }else if(strarr[i]=="("){
        counter=counter+1
        positive=c(positive,i)
      }
    }
  }
  if(counter>0){
    len=length(positive)
    saverm=c(saverm,positive[(len-counter+1):len])
  }
  return(paste0(strarr[-saverm],collapse = ''))
}
string="le(et(code())))"
getvalid(string)
string="))(("
getvalid(string)

