closestk <- function(points,k){
  len=nrow(points)
  if(len <=k){
    return(points)
  }else{
    dists=distances(points)
    return(points[quickselect(dists,k),])
  }
}
distances <- function(points){
  distance=rep(0,nrow(points))
  for(i in 1:nrow(points)){
    distance[i]=sqrt(points[i,1]^2+points[i,2]^2)
  }
  return(distance)
}
quickselect <- function(points,k){
  left = 1
  points=c(1,2,3,5,3,5)
  right = length(points)
  index = seq(1,length(points))
  curend=length(points)+1
  points = as.data.frame(cbind(points,index))
  newright=0
  newleft=0
  while(curend !=(k+1)){
    curstart=left
    curend=right
    pivot=points[curstart + floor((curend-curstart)/2),1]
    while(curstart<curend){
      print(paste0("1:",curstart,curend))
      if(points[curstart,1]<pivot){
        curstart=curstart+1
      }else{
        temp=points[curstart,]
        points[curstart,]=points[curend,]
        points[curend,]=temp
        curend=curend-1
      }
      print(points[,1])
      print(curstart)
      print(curend)
      print(pivot)
    }
    print("2")
    if(points[curend,1]<pivot){
      curend=curend+1
    }
    if(curend<(k+1)){
      left = curend
    }else{
      right = curend -1
    }
  }
  return(points[1:k,2])
}
points=matrix(c(1,0,2,0,3,0,5,0,3,0,3,0,5,0),ncol=2,byrow=TRUE)
k=4
closestk(points,k)
