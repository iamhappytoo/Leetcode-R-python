def palindromeIndex(s):
    # Write your code here
    def ispalindrome(s1):
        start, end = 0, len(s1)-1
        while start <= end:
            if s1[start]!=s1[end]:
                return False
            else:
                start += 1
                end -= 1 
        return True
    if ispalindrome(s):
        return -1
    start, end = 0, len(s)-1
    while start <= end:
        if s[start] == s[end]:
            start +=1
            end -=1
        else:
            if ispalindrome(s[(start+1):(end+1)]):
                return start
            elif ispalindrome(s[start:end]):
                return end
            else:
                return -1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
