'''
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.cache={}
        self.record=[]

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.record.remove(key)
            self.record.append(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.cache[key]=value
        if key in self.record:
            self.record.remove(key)
        self.record.append(key)
        while len(self.cache)>self.capacity:
            self.cache.pop(self.record.pop(0))
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
'''
class ListNode:
    def __init__(self,key=0,val=0):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None
    
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity=capacity
        self.cache={}
        self.head=ListNode()
        self.tail=ListNode()
        self.head.next=self.tail
        self.tail.prev=self.head
        
    def _remove(self,node):
        prev=node.prev
        new=node.next
        prev.next=new
        new.prev=prev
        
    def _insert(self,node):
        node.prev=self.head
        node.next=self.head.next
        self.head.next.prev=node
        self.head.next=node
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node=self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val
        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node=self.cache[key]
            self._remove(node)
            self._insert(node)
            node.val=value
        else:
            node=ListNode(key,value)
            self.cache[key]=node
            self._insert(node)
        if len(self.cache)>self.capacity:
            tail=self.tail.prev
            self._remove(tail)
            del self.cache[tail.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__=='__main__':
    f=LRUCache(1)
    f.get(6)
    f.get(8)
    f.put(12,1)
    f.get(2)
    f.put(15,11)
    f.put(5,2)
    f.put(1,15)
    f.put(4,2)
    f.get(4)
    f.put(15,15)