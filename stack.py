class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class Full(Exception):
    """Error when pushing elements into stack exceeds maxlen"""
    pass


class Stack:
    
    def __init__(self,maxlen=None):
        self.stack = []
        self.maxlen = maxlen
        
    def isEmpty(self):
        return self.stack == []
        
    def push(self,data):
        
        #if default constructor
        if self.maxlen == None:
            #add data to stack
            self.stack.append(data)
        #parameterized constructor
        else:
            #if the stack is less than maxlen
            if self.sizeStack() < self.maxlen:
                self.stack.append(data)
            else:
                raise Full('Stack is full')
                
        
    def pop(self):
    
        if self.isEmpty():
            raise Empty('Stack is empty')
        else:
            data = self.stack[-1]
            #delete the reference
            del self.stack[-1]
        
        return data
        
    def peek(self):
        return self.stack[-1]
        
    def sizeStack(self):
        return len(self.stack)
        
        
if __name__== "__main__":

    #default constructor
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.sizeStack())
    print("Popped: ", stack.pop(), " = 4")
    print("Popped: ", stack.pop(), " = 3")
    print(stack.sizeStack())
    print("Peek: ", stack.peek(), " = 2")
    
    #stack with a parameterized constructor
    stack = Stack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.sizeStack())
    print("Popped: ", stack.pop(), " = 4")
    print("Popped: ", stack.pop(), " = 3")
    print(stack.sizeStack())
    print("Peek: ", stack.peek(), " = 2")