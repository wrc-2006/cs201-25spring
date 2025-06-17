class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)
        if self.minstack:
            self.minstack.append(min(val,self.minstack[-1]))
        else:
            self.minstack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            self.stack.pop()
            self.minstack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minstack[-1]