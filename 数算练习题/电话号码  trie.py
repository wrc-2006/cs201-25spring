'''
def f(numbers):
    n=len(numbers)
    for i in range(n):
        for j in range(i+1,n):
            if numbers[i]==numbers[j][:len(numbers[i])]:
                return 'NO'
    return "YES"

t=int(input())
for _ in range(t):
    n=int(input())
    numbers=[]
    for __ in range(n):
        numbers.append(input())
    numbers.sort(key=lambda x:len(x))
    print(f(numbers))
'''
class TrieNode:
    def __init__(self):
        self.children={}
        self.is_end=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,number):
        node=self.root
        for i in number:
            if i not in node.children:
                node.children[i]=TrieNode()
            node=node.children[i]
            if node.is_end:
                return False
        node.is_end=True
        return len(node.children)==0
    def is_consistent(self,numbers):
        for number in numbers:
            if not self.insert(number):
                return False
        return True

t=int(input())
for _ in range(t):
    n=int(input())
    numbers=[]
    for __ in range(n):
        numbers.append(input())
    numbers.sort(key=lambda x:len(x))
    trie=Trie()
    if trie.is_consistent(numbers):
        print('YES')
    else:
        print('NO')