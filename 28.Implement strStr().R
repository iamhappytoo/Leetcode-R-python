strStr <- function(haystack, needle){
    if(needle == ''){return(0)}
    if(haystack == ''){return(-1)}
    hayarr <- unlist(strsplit(haystack, split = ''))
    needlearr <- unlist(strsplit(needle, split = ''))
    len = length(needlearr)
    for(i in 1:(length(hayarr)-(len-1))){
        temp=paste(hayarr[i:(i+len-1)],collapse='')
        if(temp == needle){
          return(i-1)
        }
    }
    return(-1)
}

haystack = ""
needle = "what"
strStr(haystack, needle)
