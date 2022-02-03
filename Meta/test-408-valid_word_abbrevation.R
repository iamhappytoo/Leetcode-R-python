digit=c('0','1','2','3','4','5','6','7','8','9')

isvalid <- function(s,abbr){
  strarr = strsplit(s,split='')
  len=length(strarr)
  abbr_arr=strsplit(abbr,split='')
  if(abbr_arr[1]=='0'){return FALSE}
  for(i in 1:(length(abbr_arr)-1)){
    if(!(abbr_arr[i]%in%digit) & (abbr_arr[i+1]=='0')){return FALSE}
  }
  abbr_arr = convert(abbr_arr)
  lenabbr=length(abbr_arr)
  curstr = 1
  curabbr = 1
  while((curstr <= len) & (curabbr <= lenabbr)){
    while(is.character(abbr_arr[[curabbr]])){
      curabbr=curabbr+1
      curstr=curstr+1
    }
    for(i in 1:abbr_arr[[curabbr]]){
      curstr=curstr+1
    }
    curstr=curstr+1
    curabbr=curabbr+1
  }
  if((curstr!=(len+1)) | (curabbr !=(lenabbr+1))){
    return(FALSE)
  }else{
    return(TRUE)
  }
}

convert <- function(strarr){
  output=list()
  curr=1
  count=1
  while(curr<=len(strarr)){
    if(!(strarr[curr]%in%digit)){
      output[[count]]=strarr[curr]
      curr=curr+1
      count=count+1
    }else{
      temp=NULL
      while(strarr[curr]%in%digit){
        temp=c(temp,strarr[curr])
        curr=curr+1
      }
      output[[count]]=as.numeric(paste0(temp))
      count=count+1
    }
  }
  return(output)
}

word = "internationalization"
abbr = "i12iz4n"