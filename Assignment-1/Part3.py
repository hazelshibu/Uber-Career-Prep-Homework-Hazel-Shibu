import unittest
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
            return "No elements remaining on stack"
    
    def isEmpty(self):
        if len(self.els) == 0:
            return True
        return False
        
    def size(self):
        return len(self.els)
    
    def printStack(self):
        string = ""
        for i in range(0,len(self.els)):
            string += str(self.els[i]) + " "
        return string
        
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

    def printQueue(self):
        string = ""
        for i in range(0,len(self.els)):
            string += str(self.els[i]) + " "
        return string

# testing
class Tests(unittest.TestCase):
    def testStack(self):
        stack1.push(5)
        stack1.push(6)
        stack1.push(7)
        stack1.push(8)
        stack1.pop()
        stack1.push(8)
        self.assertEqual(stack1.top(),8)
        self.assertEqual(stack1.size(),4)
        self.assertEqual(stack1.isEmpty(),False)
        self.assertEqual(stack1.printStack(),"5 6 7 8 ")
        for i in range(0,len(stack1.els)):
            stack1.pop()
        stack1.pop() # pop test on empty stack
        self.assertEqual(stack1.top(),"No elements remaining on stack") # top test on empty stack
        self.assertEqual(stack1.size(),0)
        self.assertEqual(stack1.isEmpty(),True)


    def testQueue(self):
        queue1.enqueue("happy")
        queue1.enqueue(10)
        queue1.enqueue(11)
        self.assertEqual(queue1.front(),11)
        self.assertEqual(queue1.rear(),"happy")
        self.assertEqual(queue1.size(),3)
        self.assertEqual(queue1.isEmpty(),False)
        self.assertEqual(queue1.printQueue(),"11 10 happy ")
        queue1.dequeue()
        self.assertEqual(queue1.printQueue(),"11 10 ")
        queue1.dequeue()
        queue1.dequeue()
        queue1.dequeue()
        self.assertEqual(queue1.rear(),"No elements remaining on queue")
        self.assertEqual(queue1.size(),0)
        self.assertEqual(queue1.isEmpty(),True)

if __name__ == '__main__':
    stack1 = Stack()
    queue1 = Queue()
    unittest.main()