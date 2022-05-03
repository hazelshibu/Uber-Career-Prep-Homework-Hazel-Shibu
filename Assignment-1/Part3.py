class Stack:
    def __init__(self):
        self.els = [] # stores the values in the list
        
    def push(self, el):
        self.els.append(el)

    def pop(self):
        if len(self.els) != 0:
            self.els.pop()
        else:
            print("No elements remaining on stack")
        
    def top(self):
        if len(self.els) != 0:
            return self.els[len(self.els)-1]
        else:
            return "No elements remaning on stack"
    
    def isEmpty(self):
        if len(self.els) == 0:
            return True
        return False
        
    def size(self):
        return len(self.els)
        
class Queue:
    def __init__(self):
        self.els = []
        
    def enqueue(self,el):
        self.els.insert(0,el)
        
    def dequeue(self):
        if len(self.els) != 0:
            self.els.pop() #FIFO
        else:
            print("No elements remaining on queue")
            
    def rear(self):
        if len(self.els) != 0:
            return self.els[len(self.els)-1]
        else:
            return "No elements remaining on queue"
            
    def front(self):
        if len(self.els) != 0:
            return self.els[0]
        else:
            return "No elements remaining on queue"
            
    def size(self):
        return len(self.els)
        
    def isEmpty(self):
        if len(self.els) == 0:
            return True
        return False

# testing
stack1 = Stack()
stack1.push(5)
stack1.push(6)
stack1.push(7)
stack1.push(8)
stack1.pop()
stack1.push(8)

print("Stack testing:")
print("top: ",stack1.top()) # top test
print("size: ",stack1.size()) # pop test

for i in range(0,len(stack1.els)):
    print("element: ",stack1.els[i])

print("Empty? ",stack1.isEmpty())
for i in range(0,len(stack1.els)):
    stack1.pop()
stack1.pop() # pop test on empty stack
print("top: ",stack1.top()) # top test on empty stack
print("Empty? ", stack1.isEmpty())
print("size: ", stack1.size())

print()
print("Queue testing:")
queue1 = Queue()
queue1.enqueue("happy")
queue1.enqueue(10)
queue1.enqueue(11)
print("front: ",queue1.front())
print("rear: ",queue1.rear())
print("size: ",queue1.size())
print("Empty? ",queue1.isEmpty())
for i in range(0,len(queue1.els)):
    print("element: ",queue1.els[i])
queue1.dequeue()
for i in range(0,len(queue1.els)):
    print("element: ",queue1.els[i])
queue1.dequeue()
queue1.dequeue()
queue1.dequeue()
print(queue1.rear())
print("size: ",queue1.size())
print("Empty? ",queue1.isEmpty())