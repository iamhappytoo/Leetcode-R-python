def preOrder(root):
    #Write your code here
    if root is None:
        return None
    print(root.info, end = ' ')
    preOrder(root.left)
    preOrder(root.right)
