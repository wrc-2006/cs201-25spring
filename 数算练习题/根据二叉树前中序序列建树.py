class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def post(root):
    ans=''
    if root:
        ans+=post(root.left)
        ans+=post(root.right)
        ans+=root.val
    return ans

def build(pre,ino):
    if not pre or not ino:
        return None
    rootval=pre[0]
    root=TreeNode(rootval)
    in_index=ino.index(rootval)
    root.left=build(pre[1:1+in_index],ino[:in_index])
    root.right=build(pre[1+in_index:],ino[1+in_index:])
    return root
    
while True:
    try:
        lst1=input()
        lst2=input()
        print(post(build(lst1,lst2)))
    except EOFError:
        break