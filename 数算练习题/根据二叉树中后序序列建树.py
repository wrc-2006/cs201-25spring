class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def preorder(root):
    ans=''
    if root:
        ans+=root.val
        ans+=preorder(root.left)
        ans+=preorder(root.right)
    return ans
def build(inorder,postorder):
    if not inorder or not postorder:
        return None
    rootval=postorder[-1]
    root=TreeNode(rootval)
    in_index=inorder.index(rootval)
    root.left=build(inorder[:in_index],postorder[:in_index])
    root.right=build(inorder[in_index+1:],postorder[in_index:-1])
    return root
inorder=input()
postorder=input()
root=build(inorder,postorder)
print(preorder(root))