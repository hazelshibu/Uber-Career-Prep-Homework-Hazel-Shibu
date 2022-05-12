import unittest
class Node:
    def __init__(self,val = None):
        self.next = None
        self.value = val

class Stack:
    def __init__(self):
        self.els = [] # stores the values in the list
        
    def push(self, el):
        self.els.append(el)

    def top(self):
        if len(self.els) != 0:
            return self.els[len(self.els)-1]
        else:
            return "No elements remaining on stack"

    def size(self):
        return len(self.els)

    def pop(self):
        if len(self.els) != 0:
            self.els.pop()
        else:
            print("No elements remaining on stack")
        
class LinkedList:
    def __init__(self,curr = None):
        self.current = curr
        
    def push(self, node):
        if self.current is not None:
            x = self.current
            while x.next is not None: #traverses the linked list
                x = x.next
            x.next = node
        else:
            self.current = node
            
    def returnedList(self):
        x = self.current
        returnedList = ""
        while x is not None:
            returnedList += str(x.value) + " "
            x = x.next
        return returnedList
    
    def reverseiterativelyLinkedList(self,currentNode):
        previousNode = None
        while currentNode != None:
            temp = currentNode.next
            currentNode.next = previousNode
            previousNode = currentNode
            currentNode = temp
        self.current = previousNode
        return self.returnedList()
    
    # not sure how to approach this
    def reverserecursivelyLinkedList(self,currentNode):
        if currentNode.next is None or currentNode is None:
            return currentNode.returnedList()
        self.reverserecursivelyLinkedList(currentNode.next)
        currentNode.next.next = currentNode
        currentNode.next = None
        return currentNode

    def reverseLinkedListStack(self):
        temp = self.current
        s = Stack()
        while temp.next is not None:
            s.push(temp)
            temp = temp.next
        self.current = temp
        for i in range(0,s.size()):
            temp.next = s.top()
            s.pop()
            temp = temp.next
        temp.next = None
        return self.returnedList()


    
class TestLinkedList(unittest.TestCase):
    def testreverseLinkedList(self):
        n = LinkedList()
        node1 = Node(5)
        n.push(node1)
        n.push(Node(6))
        n.push(Node(7))

        n2 = LinkedList()
        node2 = Node(5)
        n2.push(node2)
        n2.push(Node(6))
        n2.push(Node(7))

        n3 = LinkedList()
        n3.push(Node(5))
        n3.push(Node(6))
        n3.push(Node(7))
        self.assertEqual(n2.reverseiterativelyLinkedList(node2),'7 6 5 ')
        self.assertEqual(n3.reverseLinkedListStack(),'7 6 5 ')
        self.assertEqual(n.reverserecursivelyLinkedList(node1),'7 6 5 ')
        
if __name__ == '__main__':
    unittest.main()