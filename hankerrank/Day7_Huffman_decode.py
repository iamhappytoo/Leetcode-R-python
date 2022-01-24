def decodeHuff(root, s):
    def isleaf(node):
        if node.left or node.right:
            return False
        else:
            return True
	#Enter Your Code Here
    string = ""
    cnt = 0
    total = root.freq
    while total > 0:
        curr = root
        while not isleaf(curr):
            if int(s[cnt]) == 0:
                curr = curr.left
            else:
                curr = curr.right
            cnt += 1
        string = string + curr.data
        total -= 1
    print(string)
        
