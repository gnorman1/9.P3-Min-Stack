class MinStack(object):
    def __init__(self):
        self.data = None
        self.next = None
        self.min = 0

    def push(self, x):
      newNode = MinStack();
      newNode.data = x
      
      if self.next == None:
        newNode.min = x
        self.next = newNode
        self.min = x
      else:
        newNode.next = self.next
        self.next = newNode
        if x < self.min:
          self.min = x
          newNode.min = x
        else:
          newNode.min = self.min

        """
        :type x: int
        :rtype: None
        """
        # return
        

    def pop(self):
      nextMin = self.next.min
      temp = self.next
      self.next = self.next.next
      if self.next != None and nextMin < self.next.min:
        self.min = self.next.min
      elif self.next == None:
        self.min = 0
      del(temp)

    def top(self):
      if self.next == None:
        return None
      else:
        return self.next.data
        
    def getMin(self):
      if self.data == None and self.next == None:
        return 0
      else:
        return self.min
        
# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
param_4 = obj.getMin()
print(param_4)
obj.pop()
param_3 = obj.top()
print(param_3)
param_2 = obj.getMin()
print(param_2)
# print(param_3)
# print(param_4)