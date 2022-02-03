user_id=seq(1001,2000)
country=sample(c('US','MA','MX'),20,replace=TRUE)
facebook_age=sample(rep(10,200),20,replace=TRUE)
table1 <- as.data.frame(cbind(user_id,facebook_age))
table1$country=country
head(table1)
dat=as.Date('1998-01-01')
request=NULL
timestamp=sample(seq(as.Date('1998-01-01'),as.Date('2012-01-01'),by=29),20)
for(i in 1:20){
  request=rbind(request,sample(user_id,2))
}
request=as.data.frame(request)
colnames(request)=c("ID1","ID2")
request$timestamp=timestamp
write.table(request,'request.csv',col.names=T,row.names=F)
##Create accept csv
accept=sample(request[,1],10)
ID3=rep(0,20)
ind=sample(20,10)
ID3[ind]=request$ID1[ind]
ID3[-ind]=sample(user_id,10)
accept=as.data.frame(cbind(request$ID2,ID3))
accept$timestamp=timestamp
colnames(accept)=c("ID2","ID3","timestamp")
write.table(accept,'accept.csv',col.names=T,row.names=F)
##Create reject csv
ID4=sample(user_id,20)
ID5=sample(user_id,20)
timestamp=sample(seq(as.Date('1998-01-01'),as.Date('2020-01-01'),by=29),20)
reject=as.data.frame(cbind(ID4,ID5))
reject$timestamp=timestamp
write.table(reject,'reject.csv',col.names=T,row.names=F)
##Create delete csv
ID6=rep(0,20)
ind=sample(20,5)
ID6[ind]=accept$ID2[ind]
ID6[-ind]=sample(user_id,15)
ID7=sample(user_id,20)
timestamp=sample(seq(as.Date('1998-01-01'),as.Date('2020-01-01'),by=29),20)
delete=as.data.frame(cbind(ID6,ID7))
delete$timestamp=timestamp
write.table(delete,'delete.csv',col.names=T,row.names=F)

requestlink=paste(request$ID1,request$ID2,sep='#')
acceptlink=paste(accept$ID3,accept$ID2,sep='#')

rejectlink1=paste(reject$ID4,reject$ID5,sep='#')
rejectlink2=paste(reject$ID5,reject$ID4,sep='#')
builtlink=intersect(acceptlink,requestlink)
`%nin%`=Negate(`%in%`)
remainlink=builtlink[builtlink %nin% c(rejectlink1,rejectlink2)]
remainlink1=builtlink[!(builtlink%in%c(rejectlink1,rejectlink2))]
remainlinkarr=matrix(unlist(strsplit(remainlink,split='#')),ncol=2,byrow=TRUE)
timeoflink=as.numeric(Sys.Date()-accept[which(acceptlink %in%remainlink),3])
output=as.data.frame(cbind(remainlinkarr,timeoflink))
colnames(output)=c("friend1",'friend2','time')
