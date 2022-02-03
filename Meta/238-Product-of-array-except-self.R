product<- function(array1){
  len=length(array1)
  prodstart=rep(0,len)
  prodstart[1]=1
  for(i in 2:len){
    prodstart[i]=prodstart[i-1]*array1[i-1]
  }
  prodend=rep(0,len)
  prodend[len]=1
  for(i in (len-1):1){
    prodend[i]=prodend[i+1]*array1[i+1]
  }
  product=prodstart*prodend
  return(product)
}
array1=c(1,2,3,4)
product(array1)