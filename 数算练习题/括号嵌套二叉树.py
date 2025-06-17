class TreeNode:
    def __init__(self,val='',left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def pre(root):
    ans=''
    if root:
        ans+=root.val
        ans+=pre(root.left)
        ans+=pre(root.right)
    return ans 

def ino(root):
    ans=''
    if root:
        ans+=ino(root.left)
        ans+=root.val
        ans+=ino(root.right)
    return ans

def build(s):
    root=TreeNode(s[0])
    stack=[]
    nodes=[]
    record=[]    #判断左右子树
    cur=root
    for i in s[1:]:
        if i=='(':
            stack.append(i)
            nodes.append(cur)
        elif i==',':
            record.append(i)
        elif i==')':
            stack.pop()
            nodes.pop()
            record=[]
        elif i!="*":
            cur=TreeNode(i)
            if len(record)==0:
                nodes[-1].left=cur
            else:
                nodes[-1].right=cur
                record=[]
            
    return root
            

n=int(input())
for _ in range(n):
    s=input()
    root=build(s)
    print(pre(root))
    print(ino(root))