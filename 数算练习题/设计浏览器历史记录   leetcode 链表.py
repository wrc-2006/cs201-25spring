class ListNode:
    def __init__(self,url):
        self.url=url
        self.next=None
        self.prev=None

class BrowserHistory(object):

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.cur=ListNode(homepage)

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        newnode=ListNode(url)
        self.cur.next=newnode
        newnode.prev=self.cur
        self.cur=newnode

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps and self.cur.prev:
            steps-=1
            self.cur=self.cur.prev
        return self.cur.url

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        while steps and self.cur.next:
            steps-=1
            self.cur=self.cur.next
        return self.cur.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)