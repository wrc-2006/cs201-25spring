import heapq
class Node:
    def __init__(self,weight,char=None):
        self.weight=weight
        self.char=char
        self.left=None
        self.right=None
        
    def __lt__(self,other):
        if self.weight==other.weight:
            return self.char<other.char
        return self.weight<other.weight
    
def build_huffman(character):
    pq=[]
    for char,weight in character.items():
        heapq.heappush(pq,Node(weight,char))
    while len(pq)>1:
        left=heapq.heappop(pq)
        right=heapq.heappop(pq)
        combine=Node(left.weight+right.weight)
        combine.left=left
        combine.right=right
        heapq.heappush(pq,combine)
    return pq[0]

def encode(root):
    codes={}
    def traverse(node,code):
        if node.char:
            codes[node.char]=code
        else:
            traverse(node.left,code+'0')
            traverse(node.right,code+'1')
    traverse(root,'')
    return codes

def encoding(codes,string):
    encoded=''
    for char in string:
        encoded+=codes[char]
    return encoded

def decoding(root,string):
    decoded=''
    node=root
    for i in string:
        if i=='0':
            node=node.left
        else:
            node=node.right
        if node.char:
            decoded+=node.char
            node=root
    return decoded

n=int(input())
character={}
for _ in range(n):
    char,wei=input().split()
    character[char]=int(wei)
huffman=build_huffman(character)
codes=encode(huffman)
while True:
    try:
        string=input()
        if string[0] in ('0','1'):
            print(decoding(huffman,string))
        else:
            print(encoding(codes,string))
    except EOFError:
        break