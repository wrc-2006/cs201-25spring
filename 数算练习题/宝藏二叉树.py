class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def build(lst):
    root=TreeNode(lst[0])
    tree=[None]*(n+1)
    tree[1]=root
    for i in range(1,n+1):
        if 2*i-1<n:
            tree[2*i]=TreeNode(lst[2*i-1])
            tree[i].left=tree[2*i]
        if 2*i<n:
            tree[2*i+1]=TreeNode(lst[2*i])
            tree[i].right=tree[2*i+1]
    return root
def dp(root):
    if not root:
        return 0
    if not root.left or not root.right:
        if not root.left and root.right:
            return max(root.val,root.right.val)
        elif not root.right and root.left:
            return max(root.val,root.left.val)
        else:
            return root.val
    return max(dp(root.left)+dp(root.right),root.val+dp(root.left.left)+dp(root.left.right)+dp(root.right.left)+dp(root.right.right))

n=int(input())
lst=[int(x) for x in input().split()]
root=build(lst)
print(dp(root))