getleftmost <- function(arr){
  rows=BinaryMatrix.dimensions()[1]
  cols=BinaryMatrix.dimensions()[2]
  midcol=round(cols/2)
  startcol=1
  endcol=cols
  if(haveone(startcol,rows)==TRUE){
    return(0)
  }else if(haveone(endcol,rows)==FALSE){
    return(-1)
  }else{
    while((endcol-startcol)>1){
      if(haveone(midcol,rows)){
        endcol=midcol
        midcol=floor((startcol+endcol)/2)
      }else{
        startcol=midcol
        midcol=floor((startcol+endcol)/2)
      }
    }
    return(endcol-1)
  }
}
haveone <- function(col,rows){
  start=0
  end=rows-1
  col=col-1
  for(i in 1:rows){
    if(BinaryMatrix.get(i-1,col)){
      return(TRUE)
    }
  }
  return(FALSE)
}
BinaryMatrix.get<- function(rowa,cola){
  return(array1[rowa+1,cola+1])
}
BinaryMatrix.dimensions<- function(){
  return(c(3,4))
}
array1=matrix(c(0,0,1,1,0,0,1,1,0,0,0,1),ncol=4,byrow=TRUE)
getleftmost(array)


##Another way around (binary search of the row)
getleft <- function(arr){
rows=BinaryMatrix.dimensions()[1]
cols=BinaryMatrix.dimensions()[2]
startrow=0
startcol=cols-1
while((startrow<rows) & (startcol>=0)){
  if(BinaryMatrix.get(startrow,startcol)==0){
    startrow=startrow+1
  }else{
    startcol=startcol-1
  }
}
return(startcol+1)
}
BinaryMatrix.dimensions<- function(){
  return(dim(arr))
}
BinaryMatrix.get <- function(row,col){
  return(arr[row+1,col+1])
}
arr=matrix(c(0,0,0,1,1,1,1,1,0,0,1,1),ncol=4,byrow=TRUE)
getleft(arr)
##Another way around (binary search for each row, each time, set hi=minindex-1)


