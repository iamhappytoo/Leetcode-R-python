def replacestr(s):
    counter = s.count(' ')
    res = list(s)
    res.extend([' '] * 2 * counter)
    left = len(s) - 1
    right = len(res) - 1
    while left >= 0:
        if res[left] != ' ':
            res[right] = res[left]
            right -= 1
        else:
            res[right-2:right+1]='%20'
            right -= 3
        left = left - 1
    
    return ''.join(res)


s="i am happy"
print(replacestr(s))
    
