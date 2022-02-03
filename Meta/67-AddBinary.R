addBinary <- function(a,b){
  arra=as.numeric(unlist(strsplit(a,split='')))
  arrb=as.numeric(unlist(strsplit(b,split='')))
  if(length(arrb)<length(arra)){
    diff=length(arra)-length(arrb)
    arrb=c(rep(0,diff),arrb)
  }else{
    diff=length(arrb)-length(arra)
    arra=c(rep(0,diff),arra)
  }
  answer=as.numeric(xor(arrb,arra))
  carry=c(arrb & arra,0)
  arra=c(0,answer)
  arrb=carry
  while(1 %in% arrb){
    answer=xor(arrb,arra)
    carry[1:(length(carry)-1)]=(arrb[2:length(arrb)] & arra[2:length(arra)])
    arra=answer
    arrb=carry
  }
  if(answer[1]==0){
    answer=answer[2:length(answer)]
  }
  return(paste0(as.numeric(answer),collapse=''))
}
a="1111"
b="101"
addBinary(a,b)