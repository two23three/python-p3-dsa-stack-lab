class Stack:

    def __init__(self, items = [], limit = 100):
        self.items=[]
        self.limit = limit

        for item in items:
          if(not self.full()):
            self.items.append(item)    
        

    def isEmpty(self):

        return self.items == []

    def push(self, item):

        if(not self.full()):
            self.items.append(item)
        else:
            print("Stack is full")
       
    def pop(self):
        # if stack is empty, return none
        if self.isEmpty():
            return None
        # if stack is not empty, return the last element
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)]

    def size(self):
        return len(self.items)

    def full(self):

        if (len(self.items) >= self.limit):
            return True
        return False

    def search(self, target):
        # search from the top of the stack
        for i in reversed(range(len(self.items))):
            if self.items[i] == target:
                return len(self.items) -1  - i 
        return -1
