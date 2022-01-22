def timeConversion(s):
    # Write your code here
    if s.endswith("AM"):
        if s[0:2] == '12':
            return('00'+s[2:8])
        else:
            return(s[0:8])
    else:
        if s[0:2] == '12':
            return(s[0:8])
        else:
            hr = int(s[0:2])+12
            return(str(hr)+s[2:8])
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
